# Mykola Dotsenko

**Software Engineer · Python/Django · Backend, Data & AI Integrations**

I build reliable backend and data-intensive systems where correctness matters across external APIs, synchronization boundaries, user workflows, and imperfect real-world data.

Based in **Turku, Finland** · Open to relocation

[LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/) · [Developer profile](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html)

---

## Production engineering

My strongest work is in Python/Django backend development, multi-source integrations, data reconciliation, and production reliability.

- Reconciled **~200k CRM and contact records** with explicit validation, ambiguity handling, and idempotent processing.
- Reduced a key search flow from **3.5s to ~300ms** through backend and query-path optimization.
- Resolved **~1,600 duplicate assignment records** while strengthening repeatable ingestion and data-integrity safeguards.
- Work across APIs, databases, background processing, internal workflows, and the frontend surfaces that connect them.

Most current production work is in private client/internal repositories.

## How I engineer

- **Put correctness at the right boundary.** Prefer database/domain invariants over UI conventions when the rule must survive retries, races, or multiple clients.
- **Make uncertainty explicit.** Treat stale, ambiguous, missing, degraded, and unknown states as different states instead of hiding them behind a generic success path.
- **Treat external and AI output as untrusted input.** Validate, normalize, bound, and provide deterministic fallback where needed.
- **Keep architecture proportional.** Add abstractions, frameworks, and infrastructure only when the problem earns their cost.
- **Verify failure modes, not only happy paths.** Use automated tests, integration checks, browser flows, and production evidence to protect risky behaviour.

---

## Selected engineering work

- **[Cultural Currency Converter](https://github.com/MykolaDotsenko/cultural-currency-converter-)**  
  Django-first travel-money product with current/historical FX semantics, external-provider boundaries, PostgreSQL, HTMX, provenance-aware context, optional AI with deterministic fallback, and production-oriented backup/quality tooling.  
  `Python · Django · PostgreSQL · HTMX · TypeScript`

- **[DomoNest](https://github.com/MykolaDotsenko/wagtail-StreamField)**  
  Django + Wagtail household operating system built around cross-domain workflows, owner-scoped private state, database invariants, idempotent writes, deterministic recurrence, and server-rendered progressive enhancement.  
  `Python · Django · Wagtail · PostgreSQL · Playwright`

- **[Turku Departures](https://github.com/MykolaDotsenko/foli-live-departures)** · [Live](https://mykoladotsenko.github.io/foli-live-departures/)  
  Privacy-first transit PWA that keeps live, scheduled, stale, and unknown states distinct; handles GTFS/SIRI edge cases, repeated stops, unreliable GPS, offline use, and mobile accessibility.  
  `React · GTFS/SIRI · PWA · Playwright`

- **[JunaLippu](https://github.com/MykolaDotsenko/JunaLippu)**  
  Reliability-focused railway booking demo with segment-aware inventory, race-safe booking protected by a database constraint, concurrent-booking tests, owner-scoped reservations, and GTFS times beyond 24:00.  
  `Next.js · TypeScript · tRPC · Prisma · Playwright`

- **[Shopping Budget Companion](https://github.com/MykolaDotsenko/shopping-budget-companion)** · [Live](https://mykoladotsenko.github.io/shopping-budget-companion/)  
  Local-first shopping companion with exact-money arithmetic, versioned persistence, explicit recovery states, offline/PWA support, on-device camera features, cross-browser E2E, accessibility checks, SBOM, and build provenance.  
  `React · TypeScript · Zod · PWA · Playwright`

- **[RPS League — Reaktor](https://github.com/MykolaDotsenko/reaktor-mykola)** · [Live](https://reaktor-rps-zeta.vercel.app/)  
  Data-normalization application for a difficult legacy API: paginated ingestion, runtime validation, malformed records, duplicates, rate limits, canonical domain modelling, and a server-only API boundary.  
  `Next.js · TypeScript · Zod · Data pipelines`

---

## Core stack

**Backend & data**  
Python · Django · Django REST Framework · Wagtail · PostgreSQL · SQL · HTMX

**Frontend & product**  
TypeScript · React · Next.js · JavaScript · HTML · CSS

**Quality & delivery**  
Automated testing · Playwright · Ruff · mypy · GitHub Actions · Docker · CI/CD

## Domain edge

Before software engineering, I worked across **agriculture, greenhouse/production environments, accounting, sales, and business operations**. That background is especially useful when software has to represent real operational processes rather than idealized workflows.

I am particularly interested in **backend/data engineering, integrations, reliable AI-enabled products, and AgTech**.

---

## Contact

[LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/) · [Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html)
