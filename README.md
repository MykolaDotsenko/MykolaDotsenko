<div align="center">

# Mykola Dotsenko

**Software Engineer · Backend & Frontend · Data & AI Integrations · AgriTech**

Turku, Finland · originally from Ukraine · open to relocation

[Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html) · [LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/)

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/profile-hero-dark.svg?v=20260929-agri2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/profile-hero-light.svg?v=20260929-agri2">
  <img alt="Mykola Dotsenko — I build trustworthy software for messy reality. Python/Django, React/Next.js, data and AI integrations, with an AgriTech perspective" src="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/profile-hero-light.svg?v=20260929-agri2" width="100%">
</picture>

## About

I build software across **backend, frontend and data flows**, especially where integrations and AI-enabled features have to behave reliably in a real product.

My deepest production experience is in **Python, Django, PostgreSQL and data-heavy integrations** — APIs, domain rules, reliability and production debugging. I am usually most interested when the problem is not neat yet: two systems disagree about the same person, an API quietly goes stale, a retry creates a duplicate, or nobody is completely sure which system owns the truth.

On the frontend, I work with **TypeScript, React, Next.js and HTMX** and I am comfortable carrying a feature through to the interface — **responsive layouts, reusable component-based flows, localization, loading/error/empty states and product-facing interactions**.

I use **AI where it earns its place**: connecting model-assisted features to real workflows, attached to a clear product problem and surrounded by reliable software — deterministic business rules where they matter, explicit uncertainty, traceable data, visible failure states and an interface that makes the result understandable.

## Production engineering

I currently work as a **Software Developer at Techco / Bo in Finland**. Most of that code is private, so I focus here on the kind of engineering problems I work on rather than internal product details.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/production-flow-dark.svg?v=20260929-agri2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/production-flow-light.svg?v=20260929-agri2">
  <img alt="Production engineering flow: messy inputs through rules, state and evidence into clear interfaces and reliable workflows" src="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/production-flow-light.svg?v=20260929-agri2" width="100%">
</picture>

My production work has included **identity resolution, multi-source reconciliation, document synchronization, API integrations, retry-safe processing, source-of-truth rules, search optimization and incident investigation**.

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/capability-map-dark.svg?v=20260929-agri2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/capability-map-light.svg?v=20260929-agri2">
  <img alt="Capability map: backend, frontend, data systems and AI integrations feeding into AgriTech decision software" src="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/capability-map-light.svg?v=20260929-agri2" width="100%">
</picture>

| | |
|---|---|
| **Backend** | Python · Django · DRF · Wagtail |
| **Frontend** | TypeScript · React · Next.js · HTMX |
| **Data systems** | PostgreSQL · SQL · ETL · reconciliation pipelines · synchronization · identity resolution · validation |
| **AI & integrations** | APIs · AI-enabled flows · automation |
| **Quality & delivery** | pytest · Vitest · Playwright · Ruff · mypy · GitHub Actions · Docker |

<details>
<summary><strong>Broader hands-on stack</strong></summary>

<br>

C# · ASP.NET Core · Entity Framework Core · Angular · Node.js · SQL Server · MongoDB · Prisma · Supabase · Redis

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/celtic-divider-dark.svg?v=20260929-agri2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/celtic-divider-light.svg?v=20260929-agri2">
  <img alt="Celtic knot divider with a triquetra and wheat ears" src="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/celtic-divider-light.svg?v=20260929-agri2" width="100%">
</picture>

## From agriculture to software

I did not arrive in software through a straight line.

Before becoming a developer, I spent **8+ years across agriculture, greenhouse and food production, accounting, sales and business operations**. Later I rebuilt my career around software engineering in Finland.

**Agriculture → business & operations → software engineering → backend/data → AgriTech**

That earlier work still shapes how I build software. Accounting taught me to ask **where a number came from**. Agriculture taught me that software eventually meets weather, timing, labour, machinery and biology. Sales and operations taught me that technically correct software can still be useless if it does not fit the way people actually work.

I keep my older learning repositories public too. Some are simple and clearly early work; that is fine. They show the path instead of pretending I started at the finish line.

## AgriTech

For me, AgriTech is not a theme added to my software profile. It is where that field and business experience meets backend, frontend, data and decision-support engineering. My academic direction includes farm decision support and forecasting production/economic data.

### [PROFIT](https://github.com/MykolaDotsenko/PROFIT) — from farm data to profitable action

<div align="center">

**P** Production · **R** Revenue · **O** Operations · **F** Finance · **I** Intelligence · **T** Trade

**Farm reality → Data → Intelligence → Decision → Action → Economic effect**

<sub>Hypothetical → Modelled → Observed → Attributed → Verified</sub>

</div>

PROFIT is my longer-term AgriTech direction: connect production, operations and economics without hiding uncertainty behind a dashboard.

I want financial and agronomic logic to stay deterministic and auditable. AI can help explain, explore or interact with that logic; it should not quietly become the source of quantitative truth.

<sub>Current status: product planning, architecture and farmer-facing validation are in progress.</sub>

## Engineering principles

<table>
  <tr>
    <td width="33%" valign="top">
      <strong>Trace the source.</strong><br>
      <sub>Find where data first became wrong, not only where it became visible.</sub>
    </td>
    <td width="33%" valign="top">
      <strong>Protect the invariant.</strong><br>
      <sub>If a rule must survive retries, races or UI changes, it belongs below the UI.</sub>
    </td>
    <td width="33%" valign="top">
      <strong>Make uncertainty visible.</strong><br>
      <sub>Live, stale, missing and ambiguous are different states. I would rather show “unknown” than manufacture confidence.</sub>
    </td>
  </tr>
</table>

## Now & education

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/current-focus-dark.svg?v=20260929-agri2">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/current-focus-light.svg?v=20260929-agri2">
  <img alt="Now: production software, MSc Software Engineering, AWS architecture / Solutions Architect Associate preparation and Finnish" src="https://raw.githubusercontent.com/MykolaDotsenko/MykolaDotsenko/main/assets/current-focus-light.svg?v=20260929-agri2" width="100%">
</picture>

- **MSc Software Engineering, NTU “KhPI”** — *in progress*
- **Master’s degree in Accounting & Auditing** — *completed*
- **Current learning:** AWS architecture / Solutions Architect Associate preparation · Finnish

I am building my life and career in Finland while working, studying and learning the language.

---

<div align="center">

<sub>Software where real data, clear interfaces and real decisions matter.</sub>

</div>
