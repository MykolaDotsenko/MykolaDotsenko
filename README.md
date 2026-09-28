# Mykola Dotsenko

**Software Engineer · Python/Django · Backend, Data & API Integrations**

I build backend and data-heavy web products where external systems, imperfect data and user workflows have to stay consistent.

Based in **Turku, Finland** · Open to relocation

[Developer profile](https://mykoladotsenko.github.io/developer-profile/) ·
[Resume](https://mykoladotsenko.github.io/developer-profile/resume.html) ·
[LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/)

---

## Production work

My main stack is Python/Django and PostgreSQL. Current work includes CRM and property-data integrations, search, document flows, synchronization, production debugging and the frontend around those features.

A few concrete examples:

- reconciled roughly **200k CRM/contact records** across Kivi, OviPro and HubSpot;
- reduced one search path from **3.5s to about 300ms**;
- resolved roughly **1,600 duplicate assignment records** and tightened the ingestion rules behind them.

Most current production code lives in private client/internal repositories.

## How I work

- Trace bad data back to its source before patching what happens to appear on screen.
- Put critical rules in the database or domain layer when they must survive retries, races or multiple clients.
- Treat external API and AI output as untrusted input: validate it, bound it and provide a fallback where it matters.
- Prefer a small change in the existing stack over adding another service or abstraction without a clear reason.
- Test failure modes as well as the happy path.

---

## Selected engineering work

### [Cultural Currency Converter](https://github.com/MykolaDotsenko/cultural-currency-converter)
**Python · Django · PostgreSQL · HTMX · TypeScript**

Travel-money product with current/historical FX semantics, external-provider boundaries, provenance-aware context and graceful degradation when optional enrichment or AI is unavailable.

### [DomoNest](https://github.com/MykolaDotsenko/domonest)
**Python · Django · Wagtail · PostgreSQL · Playwright**

Household application where pantry, recipes, shopping, routines and daily planning share the same underlying state instead of drifting into separate copies.

### [Turku Departures](https://github.com/MykolaDotsenko/foli-live-departures) · [Live](https://mykoladotsenko.github.io/foli-live-departures/)
**React · GTFS/SIRI · PWA · Playwright**

Transit PWA that distinguishes live, scheduled, stale and unknown data while handling repeated stops, unreliable GPS and offline use.

### [JunaLippu](https://github.com/MykolaDotsenko/JunaLippu)
**Next.js · TypeScript · tRPC · Prisma · Playwright**

Finnish rail-booking demo with segment-aware seat inventory and a database constraint protecting concurrent reservations.

### [Shopping Budget Companion](https://github.com/MykolaDotsenko/shopping-budget-companion) · [Live](https://mykoladotsenko.github.io/shopping-budget-companion/)
**React · TypeScript · Zod · PWA · Playwright**

Shopping-budget PWA with integer money, versioned local persistence, offline use and optional on-device barcode/OCR/image-recognition helpers.

### [Tradeoff — Decision Lab](https://github.com/MykolaDotsenko/tradeoff-decision-lab) · [Live](https://tradeoff-decision-lab.vercel.app/)
**React · TypeScript · Zod**

Decision-support tool that keeps score, evidence confidence and sensitivity separate. AI can help prepare inputs; deterministic code calculates the result.

**More public work:** [RPS League — Reaktor](https://github.com/MykolaDotsenko/reaktor-rps-league) · [MovieShelf](https://github.com/MykolaDotsenko/movieshelf) · [Pakettitutka](https://github.com/MykolaDotsenko/pakettitutka)

---

## Core stack

**Backend & data**  
Python · Django · Django REST Framework · Wagtail · PostgreSQL · SQL · HTMX

**Frontend**  
TypeScript · React · Next.js · JavaScript · HTML · CSS

**Quality & delivery**  
Automated testing · Playwright · Ruff · mypy · GitHub Actions · Docker · CI/CD

## Domain background

Before software engineering, I worked across agriculture, greenhouse and food production, accounting, sales and business operations. That background is useful when software has to fit a real operational process rather than an idealized one.

I am particularly interested in backend/data engineering, integrations, reliable AI-enabled products and AgTech.

---

## Contact

[LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/) · [Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html)
