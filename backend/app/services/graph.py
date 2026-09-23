"""
Graph Service - Dependency Resolution Algorithm
Like npm/pip for standards - resolves full dependency tree
"""

from typing import Dict, List, Set, Optional, Any
from collections import deque
import json
from pathlib import Path


class StandardsGraph:
    """Knowledge graph for Indian Standards with dependency resolution."""

    def __init__(self, standards: List[Dict], relationships: List[Dict]):
        self.standards = {s["is_number"]: s for s in standards}
        self.relationships = relationships
        self._build_adjacency()

    def _build_adjacency(self):
        """Build adjacency lists for graph traversal."""
        self.outgoing = {}  # standard -> list of standards it references
        self.incoming = {}  # standard -> list of standards that reference it

        for std in self.standards.values():
            is_num = std["is_number"]
            self.outgoing[is_num] = std.get("normative_references", [])
            self.incoming[is_num] = []

        # Build incoming edges from relationships
        for rel in self.relationships:
            source = rel["source"]
            target = rel["target"]
            if target in self.incoming:
                self.incoming[target].append(source)

    def resolve_dependencies(
        self,
        standard_id: str,
        depth: int = 3,
        include_allied: bool = True
    ) -> Dict[str, Any]:
        """
        Resolve full dependency tree for a standard.

        Algorithm:
        1. BFS from starting standard
        2. Follow normative_references (REQUIRES edges)
        3. Track depth to limit traversal
        4. Build tree structure for visualization

        Returns:
            {
                "root": standard_id,
                "tree": nested tree structure,
                "flat_list": all dependencies,
                "depth_map": {standard: depth},
                "missing": standards referenced but not in database
            }
        """
        if standard_id not in self.standards:
            return {"error": f"Standard {standard_id} not found"}

        visited = set()
        depth_map = {standard_id: 0}
        missing = []

        # BFS traversal
        queue = deque([(standard_id, 0)])

        while queue:
            current_id, current_depth = queue.popleft()

            if current_id in visited or current_depth >= depth:
                continue

            visited.add(current_id)

            # Get references
            refs = self.outgoing.get(current_id, [])
            for ref in refs:
                if ref not in visited:
                    if ref in self.standards:
                        depth_map[ref] = current_depth + 1
                        queue.append((ref, current_depth + 1))
                    else:
                        missing.append(ref)

        # Add allied standards if requested
        allied = []
        if include_allied:
            for rel in self.relationships:
                if rel["source"] == standard_id and rel["type"] == "allied_standard":
                    if rel["target"] not in visited:
                        allied.append(rel["target"])
                        visited.add(rel["target"])
                        depth_map[rel["target"]] = 1

        # Build tree structure
        tree = self._build_tree(standard_id, depth_map, depth)

        return {
            "root": standard_id,
            "root_details": self.standards.get(standard_id),
            "tree": tree,
            "flat_list": list(visited),
            "depth_map": depth_map,
            "missing": missing,
            "allied": allied,
            "total_dependencies": len(visited) - 1  # exclude root
        }

    def _build_tree(self, node_id: str, depth_map: Dict, max_depth: int) -> Dict:
        """Build nested tree structure for visualization."""
        node_depth = depth_map.get(node_id, 0)

        tree_node = {
            "id": node_id,
            "details": self.standards.get(node_id, {"title": "Unknown"}),
            "depth": node_depth,
            "children": []
        }

        if node_depth < max_depth:
            refs = self.outgoing.get(node_id, [])
            for ref in refs:
                if ref in depth_map and depth_map[ref] == node_depth + 1:
                    child_tree = self._build_tree(ref, depth_map, max_depth)
                    tree_node["children"].append(child_tree)

        return tree_node

    def check_completeness(
        self,
        referenced_standards: List[str]
    ) -> Dict[str, List[str]]:
        """
        Check if all required dependencies are included.

        Used in tender audit to find missing dependencies.
        """
        referenced_set = set(referenced_standards)
        missing = {}

        for std_id in referenced_standards:
            if std_id not in self.standards:
                continue

            required = self.outgoing.get(std_id, [])
            for req in required:
                if req not in referenced_set:
                    if std_id not in missing:
                        missing[std_id] = []
                    missing[std_id].append(req)

        return missing

    def get_certification_requirements(self, standard_id: str) -> List[Dict]:
        """Get mandatory certification requirements for a standard."""
        if standard_id not in self.standards:
            return []

        std = self.standards[standard_id]
        certs = []

        if std.get("mandatory_certification"):
            certs.append({
                "type": "BIS_ISI_MARK",
                "mandatory": True,
                "description": "Product requires BIS ISI Mark certification"
            })

        return certs

    def get_standard(self, standard_id: str) -> Optional[Dict]:
        """Get details of a specific standard."""
        return self.standards.get(standard_id)

    def get_all_standards(self) -> List[Dict]:
        """Get all standards in the graph."""
        return list(self.standards.values())

    def to_vis_format(self, tree: Dict) -> Dict:
        """Convert tree to format suitable for visualization (nodes + edges)."""
        nodes = []
        edges = []

        def traverse(node, parent_id=None):
            node_id = node["id"]
            details = node.get("details", {})

            nodes.append({
                "id": node_id,
                "label": node_id,
                "title": details.get("title", "Unknown"),
                "group": node.get("depth", 0)
            })

            if parent_id:
                edges.append({
                    "from": parent_id,
                    "to": node_id,
                    "label": "requires"
                })

            for child in node.get("children", []):
                traverse(child, node_id)

        traverse(tree)
        return {"nodes": nodes, "edges": edges}


# Global instance (loaded once)
_graph_instance = None


def get_graph() -> StandardsGraph:
    """Get or create the global graph instance."""
    global _graph_instance

    if _graph_instance is None:
        data_path = Path(__file__).parent.parent.parent.parent / "data" / "sample_standards.json"
        if data_path.exists():
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            _graph_instance = StandardsGraph(
                data.get("standards", []),
                data.get("relationships", [])
            )
        else:
            _graph_instance = StandardsGraph([], [])

    return _graph_instance
