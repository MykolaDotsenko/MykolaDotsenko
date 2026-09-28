<div align="center">

# Mykola Dotsenko

### Software Engineer · Python/Django · Backend, Data & AI Integrations · AgriTech

**I build software for the moment when messy real-world data has to become a trustworthy decision.**

Turku, Finland · originally from Ukraine · open to relocation

[Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html) · [LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/)

<kbd>Python</kbd> <kbd>Django</kbd> <kbd>PostgreSQL</kbd> <kbd>APIs & integrations</kbd> <kbd>TypeScript</kbd> <kbd>React</kbd> <kbd>Decision support</kbd> <kbd>AgriTech</kbd>

</div>

---

## The short version

I am a backend/data-focused Software Engineer working mainly with **Python, Django and PostgreSQL**.

The work I like most begins where clean diagrams stop being true: two systems disagree about the same customer, an API returns stale data, a retry creates a duplicate, a GPS signal becomes unreliable, a model produces a plausible but wrong answer, or a business rule cannot afford to live only in the UI.

That usually leads me toward the same shape:

```text
messy reality
     ↓
validated state
     ↓
explicit uncertainty
     ↓
deterministic rules
     ↓
a useful next action
```

I am comfortable going end-to-end with **TypeScript, React, Next.js, HTMX and browser APIs**, but my strongest work is around **backend systems, data boundaries, integrations, domain modelling and production reliability**.

---

## The road here was not a straight line

Before software, I spent **8+ years around agriculture, greenhouse and food production, accounting, sales, customers and day-to-day business operations**.

Then I rebuilt my professional path around software engineering in Finland.

```text
fields & greenhouses
        ↓
accounting · sales · operations
        ↓
software engineering
        ↓
backend · data · integrations
        ↓
decision-support systems
        ↓
AgriTech
```

That earlier experience still affects how I write software. A database row represents something real. A duplicate customer can trigger the wrong workflow. A bad financial assumption can make a beautiful dashboard useless. A field, shipment, booking or household task has rules that existed before the code did.

I also keep learning-history repositories public on purpose. I would rather show the progression from plain HTML/CSS and early React projects to production-oriented backend and data systems than rewrite the past into a perfectly polished origin story.

---

## Production work — where correctness gets expensive

I currently work as a **Software Developer at Techco / Bo in Finland**. Most of that code is private, so I use the public profile to show the engineering patterns and outcomes I can share.

<table>
  <tr>
    <td align="center" width="33%">
      <strong>~200k</strong><br>
      <sub>CRM/contact records reconciled across Kivi, OviPro and HubSpot</sub>
    </td>
    <td align="center" width="33%">
      <strong>3.5s → ~300ms</strong><br>
      <sub>one key search path after backend/query optimization</sub>
    </td>
    <td align="center" width="33%">
      <strong>~1,600</strong><br>
      <sub>duplicate assignment records resolved while tightening ingestion rules</sub>
    </td>
  </tr>
</table>

My production work has included:

- multi-source **CRM identity resolution** and golden-record style reconciliation;
- document synchronization across property-data systems;
- Kivi / OviPro / HubSpot integrations;
- source-of-truth and ownership rules for shared external records;
- search and query-path optimization;
- idempotent/retry-safe processing;
- production incident investigation using real data rather than guesswork;
- server-rendered workflows and frontend surfaces around backend features;
- AI-enabled application features with deterministic limits and fallback behaviour.

One lesson keeps repeating:

> **Correctness depends on knowing who owns the state, what evidence is authoritative, and what the system should do when that evidence is incomplete.**

---

## AgriTech is not a side keyword for me

Agriculture is part of my professional history, not a theme I added to a portfolio later.

I have worked around **crop/greenhouse production, operational planning, accounting, sales and business economics**. My completed Master's degree in **Accounting & Auditing** gives me another lens on the same problem: production only matters commercially when costs, revenue, margin and risk are understood together.

My current **MSc in Software Engineering at NTU “KhPI”** brings those worlds together again. My study direction includes **farm decision-support software and forecasting production/economic data**.

### [PROFIT](https://github.com/MykolaDotsenko/PROFIT) — from farm data to profitable action

PROFIT is my longer-term AgriTech product direction: software that treats the farm as an economic and operational system rather than a collection of disconnected dashboards.

<table>
  <tr>
    <td align="center"><strong>P</strong><br><sub>Production</sub></td>
    <td align="center"><strong>R</strong><br><sub>Revenue</sub></td>
    <td align="center"><strong>O</strong><br><sub>Operations</sub></td>
    <td align="center"><strong>F</strong><br><sub>Finance</sub></td>
    <td align="center"><strong>I</strong><br><sub>Intelligence</sub></td>
    <td align="center"><strong>T</strong><br><sub>Trade</sub></td>
  </tr>
</table>

```text
Farm reality
    ↓
Data
    ↓
Intelligence
    ↓
Decision
    ↓
Action
    ↓
Economic effect
```

The questions matter more than the acronym:

- What is actually profitable?
- Where are costs rising?
- Which field, crop, herd, activity or customer produces the best margin?
- What decision should be taken next?
- What result was expected?
- What actually happened?
- Can the result really be attributed to the action?

For value claims I use an evidence ladder:

**Hypothetical → Modelled → Observed → Attributed → Verified**

A modelled saving is not an observed saving. An observed improvement is not automatically caused by the software. I want the product to preserve that distinction.

The same principle applies to AI: **financial and agronomic calculations should stay deterministic, testable and auditable; AI can help explain, interpret and interact with verified logic, but it should not quietly become the source of financial truth.**

The broader direction covers field crops, horticulture, greenhouse production, livestock and mixed farms. **Current status: product planning, architecture work and farmer-facing validation are in progress — this is direction, not a claim that every domain is already shipped.**

[PROFIT repository](https://github.com/MykolaDotsenko/PROFIT) · [PROFIT website work](https://github.com/MykolaDotsenko/profit-website)

---

## A few things I have built

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/MykolaDotsenko/cultural-currency-converter">
        <img src="https://raw.githubusercontent.com/MykolaDotsenko/cultural-currency-converter/master/docs/assets/cultural-currency-converter-overview.webp" alt="Cultural Currency Converter interface" width="100%">
      </a>
      <br>
      <strong>Cultural Currency Converter</strong><br>
      <sub>Django travel-money product where FX provenance, provider failure, history, local context and optional AI all have explicit boundaries.</sub>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/MykolaDotsenko/domonest">
        <img src="https://raw.githubusercontent.com/MykolaDotsenko/domonest/master/docs/images/domonest-today.png" alt="DomoNest Today dashboard" width="100%">
      </a>
      <br>
      <strong>DomoNest</strong><br>
      <sub>Django + Wagtail household system connecting pantry, recipes, shopping, meal planning and recurring routines through shared domain state.</sub>
    </td>
  </tr>
</table>

| Project | The problem I cared about |
| --- | --- |
| **[Cultural Currency Converter](https://github.com/MykolaDotsenko/cultural-currency-converter)** | A currency conversion is not useful if rate provenance, historical semantics and destination context become ambiguous when providers fail. |
| **[DomoNest](https://github.com/MykolaDotsenko/domonest)** | Household tools become noisy when pantry, recipes, shopping and routines each invent their own copy of reality. |
| **[JunaLippu](https://github.com/MykolaDotsenko/JunaLippu)** | A train seat is not simply “free” or “taken”; availability depends on overlapping journey segments and has to survive concurrent booking. |
| **[Turku Departures](https://github.com/MykolaDotsenko/foli-live-departures)** · [Live](https://mykoladotsenko.github.io/foli-live-departures/) | Realtime, scheduled, stale and unknown transit data should not look equally certain when a passenger has to act on it. |
| **[Shopping Budget Companion](https://github.com/MykolaDotsenko/shopping-budget-companion)** · [Live](https://mykoladotsenko.github.io/shopping-budget-companion/) | “How much can I still spend before checkout?” is a narrower and more useful problem than building another generic expense tracker. |
| **[Tradeoff — Decision Lab](https://github.com/MykolaDotsenko/tradeoff-decision-lab)** · [Live](https://tradeoff-decision-lab.vercel.app/) | Score, evidence confidence and sensitivity are different things; collapsing them into one number creates fake certainty. |
| **[Reel Consensus](https://github.com/MykolaDotsenko/reel-consensus)** | Movie night is often a group-compromise problem, not a single-person recommendation problem. |
| **[Pakettitutka](https://github.com/MykolaDotsenko/pakettitutka)** · [Live](https://pakettitutka.vercel.app/) | Parcel pricing is carrier-specific; when an exact price cannot be supported by published rules, the product should say so instead of inventing one. |
| **[Paddle Noir](https://github.com/MykolaDotsenko/paddle-noir)** · [Play](https://mykoladotsenko.github.io/paddle-noir/) | A deliberately playful counterweight to business software: deterministic game simulation, fixed-step physics, domain events and a neon arcade story. |
| **[RPS League — Reaktor](https://github.com/MykolaDotsenko/reaktor-rps-league)** · [Live](https://reaktor-rps-zeta.vercel.app/) | A legacy API with malformed records, duplicate IDs, looping cursors and rate limits needs a trustworthy normalization boundary before it needs more UI. |

---

## The rules I keep returning to

**Trace the source, not the symptom.**  
If bad data appears in the UI, I want to know where it first became wrong.

**Put invariants where they can survive reality.**  
If a rule must survive retries, races or several clients, a disabled button is not enough.

**Make uncertainty visible.**  
Missing, stale, ambiguous, degraded, scheduled and live are different states.

**Treat outside data as untrusted.**  
API responses, imported files, GPS, OCR and model output get validated and normalized before they become domain truth.

**Design for recovery.**  
Retries, idempotency, rollback, backup/restore, schema migration and degraded operation are part of the feature.

**Keep architecture proportional.**  
I like good architecture. I do not like architecture cosplay. A framework, queue, service or state library should solve a problem that actually exists.

**Test the path that hurts.**  
Happy-path tests are useful; concurrency, corrupted state, provider failure and deliberately broken guardrails usually teach more.

A recurring preference of mine is simple: **I would rather show “unknown” than manufacture confidence.**

---

## My working stack

<p>
  <kbd>Python</kbd>
  <kbd>Django</kbd>
  <kbd>Django REST Framework</kbd>
  <kbd>Wagtail</kbd>
  <kbd>PostgreSQL</kbd>
  <kbd>SQL</kbd>
  <kbd>HTMX</kbd>
</p>

<p>
  <kbd>TypeScript</kbd>
  <kbd>React</kbd>
  <kbd>Next.js</kbd>
  <kbd>JavaScript</kbd>
  <kbd>HTML</kbd>
  <kbd>CSS</kbd>
  <kbd>PWA / Service Workers</kbd>
</p>

<p>
  <kbd>pytest</kbd>
  <kbd>Vitest</kbd>
  <kbd>Playwright</kbd>
  <kbd>axe</kbd>
  <kbd>Ruff</kbd>
  <kbd>mypy</kbd>
  <kbd>GitHub Actions</kbd>
  <kbd>Docker</kbd>
  <kbd>CI/CD</kbd>
</p>

<details>
<summary><strong>Broader hands-on stack</strong></summary>

<br>

I have also built learning and portfolio work with **C# / ASP.NET Core / Entity Framework Core, Angular, SQL Server, MongoDB/Mongoose, Prisma, Supabase and Redis**.

That breadth is useful, but it is not the headline. My strongest current identity is still **Python/Django backend + data/integrations + product-minded systems engineering**.

</details>

---

## Education, learning and the human part

| | |
| --- | --- |
| **Work** | Software Developer — Techco / Bo, Finland |
| **Software engineering** | MSc Software Engineering — **in progress**, NTU “KhPI” |
| **Business / finance** | Master's degree in **Accounting & Auditing — completed** |
| **Domain experience** | **8+ years** across agriculture, greenhouse/production, accounting, sales and business operations |
| **Cloud** | Currently deepening AWS architecture knowledge and preparing for **AWS Solutions Architect – Associate** |
| **Languages / integration** | Based in Finland and actively learning **Finnish** alongside work and study |

I did not switch careers because the earlier years stopped mattering. They are part of why I am drawn to operational software now.

Accounting taught me to ask where a number came from. Agriculture taught me that timing, weather, labour, equipment and biological reality do not care how elegant the software model is. Sales and customer work taught me that a technically correct feature can still be useless if it does not fit the person's actual workflow.

Software engineering gave me a way to connect those lessons.

---

## What I am looking to keep doing

I am especially interested in teams working on:

**backend/data engineering · integrations · vertical SaaS · operational software · decision-support systems · reliable AI-enabled products · AgriTech**

The common thread is not an industry label. It is software where **real data, real constraints and real decisions** matter.

---

<div align="center">

### Let’s connect

[LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/) · [Portfolio](https://mykoladotsenko.github.io/developer-profile/) · [Resume](https://mykoladotsenko.github.io/developer-profile/resume.html) · [GitHub](https://github.com/MykolaDotsenko)

<sub>If a system has to survive conflicting data, retries, uncertainty or a bad day from an external API, that is usually the part I want to work on.</sub>

</div>
