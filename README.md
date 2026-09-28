<div align="center">

# Mykola Dotsenko

### Software Engineer · Python/Django · Backend, Data & AI Integrations · AgriTech

**I build software that turns imperfect real-world data into trustworthy decisions and clear next actions.**

Backend systems · data integrations · production reliability · decision-support products

**Turku, Finland** · Open to relocation

[Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html) · [LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/)

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

</div>

---

> **My recurring engineering pattern:** messy reality → validated state → explicit uncertainty → deterministic rules → reliable action.

## What I build

I am a backend/data-focused Software Engineer working mainly with **Python, Django and PostgreSQL**, with broader hands-on experience across **TypeScript, React, Next.js and full-stack web delivery**.

The problems I enjoy most are the ones where a system cannot simply assume its data is clean: multiple sources disagree, records may describe the same real-world entity, APIs fail halfway through a workflow, state becomes stale, users retry actions, or AI returns something plausible but wrong.

My strongest work sits at the intersection of:

- **backend & domain systems** — APIs, business rules, state ownership, database constraints and server-rendered workflows;
- **data & integrations** — reconciliation, identity resolution, ingestion, synchronization and external-provider boundaries;
- **production reliability** — idempotency, retries, fallbacks, recovery paths, migrations, concurrency and failure-mode testing;
- **product engineering** — turning operational data into a useful decision or next action, rather than another dashboard;
- **AI-enabled applications** — using AI where interpretation helps, while keeping critical quantitative and business logic deterministic.

## Production engineering

I currently work as a **Software Developer at Techco / Bo in Finland**. Most of my current production code is in private client/internal repositories, so the public profile focuses on the engineering patterns and measurable outcomes I can share.

Some concrete examples:

- reconciled roughly **200k CRM/contact records** across Kivi, OviPro and HubSpot with explicit validation, ambiguity handling and repeatable processing;
- reduced a key search path from **3.5 seconds to about 300 ms** through backend/query-path optimization;
- resolved roughly **1,600 duplicate assignment records** while tightening ingestion and data-integrity safeguards;
- worked on **multi-source CRM identity resolution**, document synchronization, ownership rules, search, internal workflows and production incident debugging;
- designed changes around **safe retries, rollback, degraded states and source-of-truth boundaries**, not only the happy path.

The production lesson I keep coming back to is simple: **correctness depends on knowing who owns the state, what evidence is authoritative, and what the system should do when that evidence is incomplete.**

---

## AgriTech — where my domain background becomes an engineering advantage

Before software engineering, I spent **8+ years across agriculture, greenhouse and food-production environments, accounting, sales and business operations**.

That background changes how I approach agricultural software. I do not see a farm as a collection of dashboards. I see a connected economic and operational system where production, labour, inputs, timing, risk, revenue, finance and trade all affect the quality of the next decision.

### [PROFIT](https://github.com/MykolaDotsenko/PROFIT) — from farm data to profitable action

**PROFIT** is my AgriTech product vision for decision economics across farming:

**P — Production · R — Revenue · O — Operations · F — Finance · I — Intelligence · T — Trade**

**Farm reality → Data → Intelligence → Decision → Action → Economic effect**

The product direction is built around practical questions such as:

- What is actually profitable?
- Where are costs increasing?
- Which field, crop, herd, activity or customer produces the best margin?
- What decision should be taken next?
- What economic result was expected?
- What actually happened after the decision?
- Can the result be attributed and verified?

A core principle is that financial and agronomic calculations should remain **deterministic, testable and auditable**. AI can explain, interpret and help users interact with verified logic, but it should not silently become the source of financial truth.

I also use an evidence ladder for value claims:

**Hypothetical → Modelled → Observed → Attributed → Verified**

That distinction matters: a modelled saving is not the same as an observed result, and an observed result is not automatically caused by the software.

The broader PROFIT direction covers field crops, horticulture, greenhouse production, livestock and mixed farms. **Current status: product planning, architecture design and farmer-facing validation are in progress.**

[PROFIT repository](https://github.com/MykolaDotsenko/PROFIT) · [PROFIT website repository](https://github.com/MykolaDotsenko/profit-website)

---

## Selected engineering work

| Project | What makes it interesting | Main stack |
| --- | --- | --- |
| **[Cultural Currency Converter](https://github.com/MykolaDotsenko/cultural-currency-converter)** | Django-first travel-money product with current/historical FX semantics, provider boundaries, provenance-aware context, account/local state, graceful degradation and optional AI with deterministic fallback. | Python · Django · PostgreSQL · HTMX · TypeScript |
| **[DomoNest](https://github.com/MykolaDotsenko/domonest)** | Household operating system where pantry, recipes, shopping, meal planning and routines share connected domain state instead of becoming isolated CRUD modules. | Python · Django · Wagtail · PostgreSQL · Playwright |
| **[Turku Departures](https://github.com/MykolaDotsenko/foli-live-departures)** · [Live](https://mykoladotsenko.github.io/foli-live-departures/) | Privacy-first transit PWA that keeps live, scheduled, stale and unknown states distinct while handling GTFS/SIRI edge cases, repeated stops, unreliable GPS and offline use. | React · GTFS/SIRI · PWA · Playwright |
| **[Shopping Budget Companion](https://github.com/MykolaDotsenko/shopping-budget-companion)** · [Live](https://mykoladotsenko.github.io/shopping-budget-companion/) | “Know what is left before checkout”: exact-money arithmetic, versioned persistence, recovery states, offline/PWA behavior and optional on-device barcode, OCR and visual-recognition helpers. | React · TypeScript · Zod · PWA · Playwright |
| **[Reel Consensus](https://github.com/MykolaDotsenko/reel-consensus)** | Group movie decision engine: hard vetoes, participant scoring, fairness strategies and visible trade-offs. AI may parse fuzzy intent; deterministic code makes the final ranking. | React · TypeScript · Vite · Supabase · Playwright |
| **[Tradeoff — Decision Lab](https://github.com/MykolaDotsenko/tradeoff-decision-lab)** · [Live](https://tradeoff-decision-lab.vercel.app/) | Explainable decision support that keeps score, evidence confidence and sensitivity separate instead of turning uncertainty into one fake-precise number. | React · TypeScript · Zod |
| **[JunaLippu](https://github.com/MykolaDotsenko/JunaLippu)** | Railway-booking demo with segment-aware inventory, concurrent-booking protection and database constraints enforcing the real invariant. | Next.js · TypeScript · tRPC · Prisma · Playwright |
| **[RPS League — Reaktor](https://github.com/MykolaDotsenko/reaktor-rps-league)** · [Live](https://reaktor-rps-zeta.vercel.app/) | Legacy-API normalization project built around malformed records, duplicates, cursor pagination, rate limits and a canonical domain model. | Next.js · TypeScript · Zod · Data pipelines |

More experiments and learning history remain public too — from **C#/.NET, Angular and MongoDB** projects to small dependency-free JavaScript apps, accessibility exercises and creative work such as [Paddle Noir](https://github.com/MykolaDotsenko/paddle-noir). I keep that history visible because it shows the progression, not just the latest snapshot.

---

## The product lens behind the code

I tend to design products around a **decision moment**, not around a software category.

- A currency converter becomes: **what does this amount mean locally, and how trustworthy is the context?**
- A transit app becomes: **what should the passenger do now, and is the realtime data good enough to act on?**
- A shopping tracker becomes: **how much is really left before checkout?**
- A movie recommender becomes: **what compromise can this group actually accept?**
- A farm dashboard becomes: **which decision changes the economics, and can the effect be verified?**

That is why many of my projects share the same shape:

**real-world data → explicit state → uncertainty → decision support → user action → measurable outcome**

---

## How I engineer

- **Trace the source before patching the symptom.** Bad data on screen often started much earlier in the pipeline.
- **Protect invariants at the right layer.** If a rule must survive retries, races or multiple clients, UI convention is not enough.
- **Make uncertainty visible.** Missing, stale, ambiguous, scheduled, degraded and live are different states.
- **Treat external and AI output as untrusted input.** Validate, normalize, bound and fall back deterministically when the workflow depends on it.
- **Design for retries and recovery.** Idempotency, rollback, versioned persistence and degraded operation are part of the feature.
- **Keep architecture proportional.** I prefer the smallest design that reliably protects the user and domain rules; complexity has to earn its cost.
- **Test the failure path.** Unit and browser tests matter, but so do integration checks, concurrency cases, real-data probes and deliberate attempts to break the guardrails.

---

## Core stack

**Backend & data**  
Python · Django · Django REST Framework · Wagtail · PostgreSQL · SQL · HTMX

**Frontend & product**  
TypeScript · React · Next.js · JavaScript · HTML · CSS · PWA / Service Workers

**Quality & delivery**  
pytest / Django tests · Vitest · Testing Library · Playwright · axe · Ruff · mypy · ESLint · GitHub Actions · Docker · CI/CD

**Additional hands-on experience**  
C# · ASP.NET Core · Entity Framework Core · Angular · SQL Server · MongoDB · Prisma · Supabase · Redis

**Current learning / deeper focus**  
AWS architecture · data engineering · system design · observability · reliable AI-enabled applications

---

## Background & education

- **Software Developer — Techco / Bo**, Finland
- **MSc Software Engineering — in progress**, NTU “KhPI”
- **Master’s degree in Accounting & Auditing — completed**
- **8+ years of previous domain experience** across agriculture, greenhouse/production, accounting, sales and business operations

That combination is why I am especially interested in **backend/data engineering, integrations, decision-support software, reliable AI-enabled products and AgriTech**.

---

## Let’s connect

[LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/) · [Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html) · [GitHub](https://github.com/MykolaDotsenko)

<sub>I care about software that survives contact with real data, real users and real operational constraints.</sub>
