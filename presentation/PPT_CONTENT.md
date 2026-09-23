# SIH Finals Presentation: StandardsAI
## AI-Powered Recommendation Engine for Indian Standards
### Problem ID: 26108 | Ministry: DoCA

---

# SLIDE 1: TITLE SLIDE

## Content
**Project Name:** StandardsAI  
**Tagline:** "Intelligent Standards Discovery for Smart Procurement"

**Visual Layout:**
- Large project logo/name at center
- Tagline below
- Team name and institution at bottom
- SIH 2026 logo + DoCA logo

**Text to Display:**
```
StandardsAI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI-Powered Recommendation Engine for 
Identifying Applicable Indian Standards

Problem Statement ID: 26108
Ministry of Consumer Affairs | Department of Consumer Affairs

Team: [Your Team Name]
Institution: [Your College]
```

**Speaker Notes (30 seconds):**
> "Good morning/afternoon. We are Team [Name] from [College]. Today we present StandardsAI - an AI-powered solution that helps government procurement officers identify the right Indian Standards in seconds, not hours. Let's begin with why this matters."

---

# SLIDE 2: THE PROBLEM

## Content
**Title:** The Hidden Crisis in Government Procurement

**Key Statistics (make these BIG):**
- ₹20+ Lakh Crore - Annual government procurement spend
- 22,000+ - Published BIS standards
- 40% - Procurement disputes involve standards issues (estimated)

**The Pain Point:**
"Procurement officers must reference correct standards in tenders. 
But finding the RIGHT standard among 22,000 is like finding a needle in a haystack."

**Visual:** 
- Split screen: Left shows mountain of documents, Right shows confused officer
- OR: Infographic showing the scale (22,000 standards stacked)

**Speaker Notes (45 seconds):**
> "Every year, the Indian government spends over 20 lakh crore rupees on procurement - from steel pipes to LED bulbs to medical equipment. Every tender must reference the correct Indian Standards to ensure quality. But here's the problem: there are over 22,000 BIS standards, and this number grows by 500 every year. The average procurement officer knows maybe 100 standards. The result? Tenders reference wrong standards, outdated versions, or miss critical safety standards entirely. This leads to quality failures, legal disputes, and ultimately, taxpayer money wasted."

---

# SLIDE 3: CURRENT STATE - WHY EXISTING SOLUTIONS FAIL

## Content
**Title:** The Gap We're Filling

**Comparison Table:**

| Aspect | BIS Website | Manual Search | Our Solution |
|--------|-------------|---------------|--------------|
| Search Type | Keyword only | Expert memory | Semantic AI |
| Allied Standards | Manual lookup | Trial & error | Auto-linked |
| Version Check | Manual | Often missed | Automatic |
| Time Required | 30+ minutes | Hours/Days | < 3 seconds |
| Accuracy | Low | Variable | 95%+ |

**Key Insight Box:**
"BIS website returns 500+ results for 'steel pipes' - 
which one applies to YOUR specific use case?"

**Visual:**
- Screenshot of BIS website search showing overwhelming results
- Arrow pointing to "No context understanding"

**Speaker Notes (40 seconds):**
> "Let's look at what exists today. The BIS website offers keyword search - type 'steel pipes' and you get hundreds of results with no context. Which one is for drinking water? Which for industrial use? Which for high pressure? You have to read each one. There's no system that understands your CONTEXT. GeM portal references standards but has no recommendation engine. The current process is manual, time-consuming, and error-prone. This is the gap we fill."

---

# SLIDE 4: OUR SOLUTION - THE "AHA!" MOMENT

## Content
**Title:** StandardsAI - Standards Expert on Call 24/7

**One-Liner (make this HUGE):**
> "Describe your product. Get complete standards package. In seconds."

**The Magic:**
```
Input: "Steel pipes for drinking water supply in coastal area"

Output:
├── IS 1239 - Steel Tubes (Primary)
├── IS 10500 - Drinking Water Spec (Safety)
├── IS 4736 - Zinc Coating (Corrosion - coastal!)
├── IS 4984 - HDPE Pipes (Alternative)
└── BIS Product Certification Required ✓
```

**3 Key Innovations:**
1. **Semantic Understanding** - Understands "coastal" means corrosion protection needed
2. **Knowledge Graph** - Auto-links allied standards, test methods, safety requirements  
3. **Always Current** - Flags outdated standards, shows amendments

**Visual:**
- Clean input/output diagram
- Show the "understanding" happening (brain icon processing)

**Speaker Notes (45 seconds):**
> "This is StandardsAI. You describe your product in plain language - even in Hindi - and our AI understands the CONTEXT, not just keywords. Notice how 'coastal area' triggered corrosion-resistant coating standards? That's semantic understanding. But we don't just give you one standard - we give you the COMPLETE PACKAGE: the main standard, plus all allied standards for testing, safety, and installation. And we flag if certification is mandatory. It's like having a standards expert sitting next to you, available 24/7."

---

# SLIDE 5: HOW IT WORKS - TECHNICAL OVERVIEW

## Content
**Title:** Under the Hood - How StandardsAI Thinks

**Simple Flow Diagram:**
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   INPUT     │    │    AI       │    │   VECTOR    │    │   GRAPH     │
│  Product    │ -> │  Embedding  │ -> │   Search    │ -> │  Expansion  │
│ Description │    │  Generation │    │  (Semantic) │    │  (Allied)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                │
                   ┌─────────────┐    ┌─────────────┐           │
                   │   OUTPUT    │ <- │    LLM      │ <---------┘
                   │  Standards  │    │  Re-ranking │
                   │  Package    │    │  & Explain  │
                   └─────────────┘    └─────────────┘
```

**Tech Highlights (icons + one-liners):**
- Vector Embeddings: Converts text to meaning
- Knowledge Graph: 22,000 standards connected
- LLM Reasoning: Explains WHY these standards apply

**Visual:**
- Animated flow if possible
- Keep it VISUAL, minimal text

**Speaker Notes (40 seconds):**
> "Here's how it works. Your query is converted into a semantic vector - a mathematical representation of MEANING, not just words. We search our database of 22,000 standards using similarity matching. But here's the key innovation: we then traverse our Knowledge Graph to find ALL related standards - the test methods, safety standards, terminology standards. Finally, an LLM ranks and explains the results. The entire process takes under 3 seconds."

---

# SLIDE 6: KEY FEATURES

## Content
**Title:** What Makes StandardsAI Powerful

**6 Features with Icons:**

1. **Semantic Search** 
   - Understands context, not just keywords
   - "Water pipes" vs "Drinking water pipes for schools"

2. **Allied Standards Graph**
   - Auto-discovers normative references
   - Test methods, safety, installation standards

3. **Version Tracking**
   - Always shows latest version
   - Alerts for amendments and withdrawals

4. **Certification Mapping**
   - Flags mandatory BIS/CRS/Hallmark requirements
   - Compliance checklist

5. **Multilingual Support**
   - Hindi, Tamil, Telugu + 19 more languages
   - Powered by Bhashini

6. **GeM Integration Ready**
   - API for direct integration
   - Works within existing workflow

**Visual:**
- 2x3 grid of feature cards with icons
- Clean, minimal design

**Speaker Notes (40 seconds):**
> "Six key features differentiate us. First, semantic search that understands context. Second, our knowledge graph that automatically finds all related standards. Third, we always show the latest version and flag updates. Fourth, we map mandatory certification requirements - critical for compliance. Fifth, multilingual support powered by Bhashini - a government initiative. And sixth, we're API-ready for GeM integration. This isn't a standalone tool - it fits into existing workflows."

---

# SLIDE 7: TECHNOLOGY STACK

## Content
**Title:** Built for Government Scale

**Architecture Diagram (Simplified):**
```
┌────────────────────────────────────────────────────────────┐
│                    FRONTEND (Next.js)                      │
│              Government Accessible, GIGW Compliant         │
└────────────────────────────────────────────────────────────┘
                              │
┌────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                       │
│           ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│           │ Embedding│ │  Search  │ │   LLM    │          │
│           │ Service  │ │  Engine  │ │ Reasoning│          │
│           └──────────┘ └──────────┘ └──────────┘          │
└────────────────────────────────────────────────────────────┘
                              │
┌────────────────────────────────────────────────────────────┐
│                    DATA LAYER                              │
│    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│    │ ChromaDB │    │  Neo4j   │    │PostgreSQL│          │
│    │ (Vectors)│    │ (Graph)  │    │(Metadata)│          │
│    └──────────┘    └──────────┘    └──────────┘          │
└────────────────────────────────────────────────────────────┘
```

**Key Points (badges):**
- 100% Open Source Core
- Data Sovereignty - All data in India
- Bhashini + IndiaAI Aligned
- NIC Cloud Ready

**Visual:**
- Clean architecture diagram
- Government/India colors (saffron, green accents)

**Speaker Notes (35 seconds):**
> "Our technology stack is designed for government deployment. The core is 100% open source - no vendor lock-in. All data stays in India - complete data sovereignty. We integrate with Bhashini for multilingual support - aligning with IndiaAI initiatives. The stack is Neo4j for the knowledge graph, FastAPI for the backend, and Next.js for an accessible frontend. We can deploy on NIC Cloud tomorrow."

---

# SLIDE 8: DEMO / SCREENSHOTS

## Content
**Title:** See It In Action

**Option A - If Live Demo:**
Show 3 scenarios live:
1. Simple text query (LED bulbs)
2. Complex context query (coastal steel pipes)
3. Hindi voice query

**Option B - Screenshots:**

**Screenshot 1: Search Interface**
- Clean search bar
- "Try: Steel pipes for drinking water supply"

**Screenshot 2: Results View**
- Primary standards with scores
- Allied standards tree
- Certification badges

**Screenshot 3: Graph Visualization**
- Interactive standards relationship graph
- Click to explore connections

**Screenshot 4: Hindi Query**
- Shows "सड़क निर्माण के लिए सीमेंट"
- Results in English with Hindi labels

**Speaker Notes (60 seconds for live demo, 40 for screenshots):**
> "Let me show you StandardsAI in action. [Demo Query 1] I type 'LED bulbs for government office' - within 2 seconds, we get IS 16102 for LED lamps, IS 10322 for luminaires, and a BIS certification flag. [Demo Query 2] Now a complex query: 'corrosion resistant pipes for coastal drinking water' - notice how it understands coastal means marine environment and adds coating standards. [Demo Query 3] Finally, in Hindi: 'सड़क निर्माण के लिए सीमेंट' - cement for road construction - and we get OPC, PSC, and PPC standards with usage guidance."

---

# SLIDE 9: SECURITY & COMPLIANCE

## Content
**Title:** Enterprise-Grade Security, Government Compliant

**Security Features (with shield icons):**

| Feature | Implementation |
|---------|----------------|
| Data Residency | 100% in India - NIC Cloud |
| Encryption | TLS 1.3 + AES-256 at rest |
| Authentication | DigiLocker/eSign SSO |
| Access Control | Role-Based (RBAC) |
| Audit Logging | Complete trail for compliance |
| PII Protection | No personal data stored |

**Compliance Badges:**
- GIGW Compliant
- IT Act 2000 Compliant  
- MeitY Guidelines Followed
- Regular VAPT

**Key Message:**
"Tender documents are processed in memory - never stored. 
Your procurement data stays YOUR data."

**Visual:**
- Shield/lock icons
- India map with "Data stays here" marker

**Speaker Notes (30 seconds):**
> "Security is non-negotiable for government systems. All data resides in India on NIC Cloud. We use industry-standard encryption. Authentication integrates with DigiLocker. Critically, tender documents you upload are processed in memory and never stored - your procurement data stays your data. We follow GIGW guidelines and conduct regular security audits."

---

# SLIDE 10: SCALABILITY

## Content
**Title:** Built to Scale with India's Procurement Needs

**Growth Projection Chart:**

```
Queries/Day
   │
500K│                              ╭────── Year 3
   │                         ╭────╯
   │                    ╭───╯
50K │              ╭───╯                   Year 1
   │         ╭───╯
1K  │────────╯                              Now
   └─────────────────────────────────────────────
         Q1    Q2    Q3    Q4    Y2    Y3
```

**Scaling Architecture:**
- Kubernetes auto-scaling
- Multi-region deployment (Delhi, Mumbai, Hyderabad)
- Response time: < 3 seconds at any scale

**Numbers:**
| Metric | Current | Year 1 | Year 3 |
|--------|---------|--------|--------|
| Daily Queries | 1,000 | 50,000 | 500,000 |
| Concurrent Users | 50 | 500 | 5,000 |
| Response Time (p95) | < 3s | < 2s | < 1s |

**Visual:**
- Growing graph
- India map with region markers

**Speaker Notes (30 seconds):**
> "We're built to scale. Starting with 1,000 queries per day, we can scale to half a million daily queries by year 3. Our Kubernetes architecture auto-scales based on demand. We deploy across multiple regions for low latency nationwide. Even at full scale, response time stays under 3 seconds. This can serve every procurement officer in India."

---

# SLIDE 11: IMPACT & METRICS

## Content
**Title:** Measurable Impact on Procurement Quality

**Before/After Comparison:**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Research Time | 2-4 hours | < 5 minutes | 95% faster |
| Standards Found | 1-2 | 5-8 (complete) | 3x more |
| Version Accuracy | 60% | 99% | Near perfect |
| Compliance Flags | Often missed | Always shown | 100% |

**Projected Impact (make these BIG):**
- **80%** reduction in standards research time
- **95%** accuracy in recommendations  
- **50%** reduction in standards-related disputes
- **3x** more allied standards referenced per tender

**Value Statement:**
"Every correctly referenced standard prevents a procurement dispute.
Every dispute prevented saves lakhs in litigation."

**Visual:**
- Before/after split screen
- Big impact numbers with icons

**Speaker Notes (35 seconds):**
> "Let's talk impact. Today, researching standards takes 2-4 hours. With StandardsAI, under 5 minutes. We find not 1-2 standards but the complete package of 5-8 related standards. Version accuracy goes from 60% to 99%. Most importantly, we project a 50% reduction in standards-related procurement disputes. Every dispute prevented saves lakhs in litigation costs and months of delays. This is real, measurable value."

---

# SLIDE 12: ROADMAP

## Content
**Title:** From Hackathon to National Deployment

**Timeline:**

```
Phase 1 (Now)          Phase 2 (3 months)       Phase 3 (12 months)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   │                        │                         │
   │  MVP Demo              │  Pilot Program          │  National Rollout
   │  - 500 standards       │  - 22,000 standards     │  - GeM Integration
   │  - Core features       │  - GeM API pilot        │  - Mobile App
   │  - Web interface       │  - User feedback        │  - All 22 languages
   │                        │  - Security audit       │  - Analytics dashboard
   │                        │                         │
   ▼                        ▼                         ▼
```

**Key Milestones:**
- **Month 3:** Full standards database
- **Month 6:** GeM pilot with select departments
- **Month 9:** Security certification
- **Month 12:** National deployment

**Visual:**
- Horizontal timeline with milestone markers
- Icons for each phase

**Speaker Notes (30 seconds):**
> "Our roadmap is realistic and achievable. Today, we demonstrate the MVP with 500 standards. In 3 months, we ingest all 22,000 BIS standards and begin a pilot with GeM. By 6 months, select departments test the integration. Month 9, security certification. By 12 months, we're ready for national deployment with mobile apps and full multilingual support. We've thought through every step."

---

# SLIDE 13: BUSINESS MODEL (Optional - if asked)

## Content
**Title:** Sustainable Model for Long-term Impact

**Three Tiers:**

| Segment | Model | Revenue |
|---------|-------|---------|
| **Government** | Free (Public Good) | Funded by ministry |
| **Private Sector** | Freemium | 50 free queries/month, then subscription |
| **API/Enterprise** | Usage-Based | Per-query pricing for ERP integrations |

**Why This Works:**
- Core mission (government) remains free
- Private sector adoption generates sustainability
- API licensing creates integration ecosystem

**Potential Scale:**
- 100,000 government users (free)
- 10,000 private subscribers  
- 50 enterprise API clients

**Visual:**
- Three-tier pyramid
- Government at base (largest, free)

**Speaker Notes (25 seconds):**
> "For sustainability: government use is always free - this is a public good. Private enterprises get 50 free queries monthly, then pay a subscription. Enterprise clients pay for API access to integrate into their procurement systems. This creates a sustainable model while keeping the core mission free for government."

---

# SLIDE 14: TEAM

## Content
**Title:** The Team Behind StandardsAI

**Team Grid (2x3 or as needed):**

| Photo | Name | Role | Expertise |
|-------|------|------|-----------|
| [Photo] | [Name 1] | ML Engineer | NLP, Embeddings, LLMs |
| [Photo] | [Name 2] | Backend Lead | FastAPI, Databases, APIs |
| [Photo] | [Name 3] | Frontend Dev | React, Next.js, UI/UX |
| [Photo] | [Name 4] | Data Engineer | ETL, Scraping, Neo4j |
| [Photo] | [Name 5] | Domain Expert | Standards, Procurement |
| [Photo] | [Name 6] | Design & Pitch | Presentation, Demo |

**Team Credentials:**
- [Combined relevant experience/achievements]
- [Any relevant projects or competitions]

**Mentor:**
- [Mentor name and expertise if applicable]

**Visual:**
- Professional photos in circles
- Role badges below each

**Speaker Notes (20 seconds):**
> "We are a team of 6 with complementary skills - ML expertise for the AI engine, full-stack development capability, and domain knowledge in standards and procurement. We've worked together on [previous project] and bring [X] combined experience. Our mentor [Name] provides guidance on [area]."

---

# SLIDE 15: THANK YOU & CONTACT

## Content
**Title:** Thank You

**Recap (3 bullet points):**
- AI-powered semantic search for 22,000+ BIS standards
- Complete standard packages with allied standards & certifications
- Built for government scale, security, and integration

**Call to Action:**
"Every correctly referenced standard prevents a procurement dispute."

**Contact & Links:**
- GitHub: github.com/[your-repo]
- Demo: [demo-url if hosted]
- Email: [team-email]
- LinkedIn: [Team LinkedIn]

**QR Code:** Link to demo or documentation

**Visual:**
- Clean, minimal
- Large QR code for easy scanning
- Team logo

**Speaker Notes (15 seconds):**
> "In summary, StandardsAI transforms standards discovery from hours to seconds, ensures complete coverage with allied standards, and is ready for government deployment. We're excited to bring this to every procurement officer in India. Thank you. We welcome your questions."

---

# APPENDIX: ANTICIPATED QUESTIONS & ANSWERS

## Q1: "How do you get access to BIS standards data?"
**A:** "BIS publishes a public catalog at services.bis.gov.in with standard metadata - titles, scopes, numbers. This is publicly accessible. For the MVP, we scrape this catalog. For production, we propose a formal data partnership with BIS - they benefit from wider standards adoption. The full standard PDFs are available at standardsbis.bsbedge.com, many for free."

## Q2: "What about accuracy? Can AI make mistakes?"
**A:** "Great question. We use RAG - Retrieval Augmented Generation - which grounds the AI in actual standards data, not hallucinations. Every recommendation comes with citations and relevance scores. For critical decisions, we recommend human review. The system assists, it doesn't replace human judgment. Our accuracy target is 95% measured against expert curations."

## Q3: "How is this different from just using ChatGPT?"
**A:** "Three key differences: First, ChatGPT doesn't have updated BIS standards - its knowledge is cutoff. We have real-time data. Second, ChatGPT can't traverse our knowledge graph to find allied standards - that's custom engineering. Third, ChatGPT can't tell you if a standard was withdrawn or amended yesterday. We can. We're domain-specific, always current, and relationship-aware."

## Q4: "What about security for sensitive tender information?"
**A:** "Tender documents are processed in memory and never persisted. We can offer an on-premise deployment option for highly sensitive use cases. All data stays in India. We follow GIGW guidelines and will undergo VAPT certification before production. For the most sensitive queries, we can use self-hosted LLMs instead of external APIs."

## Q5: "How do you handle non-English queries?"
**A:** "We integrate with Bhashini - the government's multilingual AI initiative. Queries in Hindi or any of the 22 scheduled languages are translated, processed, and results can be displayed in the original language. This is critical for adoption across India."

## Q6: "What if BIS updates a standard tomorrow?"
**A:** "Our data pipeline runs daily. BIS publishes weekly bulletins announcing new and revised standards. We ingest these automatically. When a referenced standard is superseded, we flag it in the system. Users who previously searched for that standard can be notified. Staying current is a core feature, not an afterthought."

## Q7: "Can this integrate with GeM?"
**A:** "Yes, we're API-first. Our REST API can be called from GeM's tender creation workflow. When a procurement officer describes a product, GeM can call our API and display recommended standards inline. We've designed the API contract with GeM integration in mind. We'd love to pilot with GeM post-hackathon."

---

# DESIGN TIPS FOR PPT

## Color Palette
- **Primary:** Deep Blue (#1a365d) - Trust, Government
- **Secondary:** Saffron (#ff6b35) - India, Energy
- **Accent:** Green (#38a169) - Success, Go
- **Background:** White or Light Gray (#f7fafc)
- **Text:** Dark Gray (#2d3748)

## Fonts
- **Headlines:** Bold Sans-serif (Poppins, Inter, or Roboto)
- **Body:** Regular Sans-serif
- **Code/Data:** Monospace (Fira Code, JetBrains Mono)

## Design Principles
1. **One idea per slide** - Don't overcrowd
2. **Visual > Text** - Use diagrams, icons, charts
3. **Big numbers** - Make statistics impossible to miss
4. **Consistent alignment** - Grid-based layout
5. **Breathing room** - White space is your friend

## Animation (if used)
- Keep it minimal
- Fade or appear only
- No spinning, bouncing, or flying text
- Use to reveal information sequentially

---

# PRESENTATION TIMING (10 minutes total)

| Slide | Time | Cumulative |
|-------|------|------------|
| 1. Title | 0:30 | 0:30 |
| 2. Problem | 0:45 | 1:15 |
| 3. Current State | 0:40 | 1:55 |
| 4. Solution | 0:45 | 2:40 |
| 5. How It Works | 0:40 | 3:20 |
| 6. Features | 0:40 | 4:00 |
| 7. Tech Stack | 0:35 | 4:35 |
| 8. Demo | 1:00 | 5:35 |
| 9. Security | 0:30 | 6:05 |
| 10. Scalability | 0:30 | 6:35 |
| 11. Impact | 0:35 | 7:10 |
| 12. Roadmap | 0:30 | 7:40 |
| 13. Business Model | 0:25 | 8:05 |
| 14. Team | 0:20 | 8:25 |
| 15. Thank You | 0:15 | 8:40 |
| **Buffer** | 1:20 | 10:00 |

---

*Good luck! You've got this!*
