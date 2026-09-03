---
name: saas-growth-diagnosis
description: Inspect a SaaS product and diagnose growth bottlenecks from traffic through landing-page conversion, activation, trial-to-paid conversion, pricing, and retention, or assess pre-launch measurement readiness. Use when a SaaS founder or growth owner wants to identify the earliest broken stage, understand likely causes, or prioritize measurable experiments. Do not use for channel execution, UI implementation, or generic startup ideation.
---

# SaaS Growth Diagnosis

Inspect the product and accessible evidence first, then turn what is available into a useful diagnosis: identify the earliest meaningful bottleneck, show the evidence and uncertainty, and recommend the next three experiments.

The method is based on Mengqi Pei's product work at Alibaba and TikTok and growth-diagnosis experience with 30+ SaaS products.

## Operating principles

- Diagnose in funnel order: traffic quality → landing-page conversion → activation → trial-to-paid and pricing → retention and expansion.
- Discover before asking. Inspect the current workspace, supplied files, reachable product surfaces, and authorized read-only data before requesting information from the user.
- Find the earliest broken stage before optimizing a downstream symptom.
- Treat benchmarks as directional context, never as universal pass/fail rules.
- Separate observed facts, calculated metrics, hypotheses, and missing evidence.
- Do not invent product facts, analytics, user behavior, benchmarks, or causal explanations.
- Deliver value with partial information. Never begin with a questionnaire or ask the user to manually retrieve information the agent can access.
- Recommend experiments rather than promising outcomes. Never guarantee a 2–3× lift.
- Respond in the user's language unless they request another language.
- Diagnose and prioritize; do not claim to execute ads, redesign interfaces, configure analytics, or run experiments unless the user separately requests and authorizes that work.

## Start with autonomous discovery

The user may provide only “diagnose this product,” a repository path, or a URL. Use the context already provided and do not ask them to choose a mode.

1. Resolve the target product from the current workspace, supplied path, URL, screenshot, or conversation.
2. Read [references/intake-and-metrics.md](references/intake-and-metrics.md) and inspect all safe, relevant, read-only evidence already available.
3. Determine whether the product is live with behavioral evidence, live without accessible behavioral evidence, or pre-launch.
4. State briefly what was inspected and what remains unknowable from those sources.
5. Ask one high-leverage question only when its answer could change the diagnosis or next action. Never send a form or a list of metrics for the user to fill out.
6. If the user does not answer, proceed with a provisional diagnosis and an evidence-collection action.

Repository access can reveal intended behavior, event definitions, routes, onboarding logic, pricing configuration, and obvious friction. It does not prove how production users behave. Analytics code is not analytics data.

Do not read or reveal secret values. Do not query private production systems, create accounts, submit forms, or mutate external state without appropriate access and authorization.

## Choose the entry path

### Quick diagnosis

Use when the product is live but reliable behavioral data is not accessible.

1. Infer the product, target customer, intended core value, acquisition source, and business model from available evidence.
2. Inspect the public experience and repository when accessible.
3. Give a provisional diagnosis and confidence level.
4. Separate implementation evidence from actual user-behavior evidence.
5. Ask at most one decision-changing question, or give a smallest-evidence collection plan rather than stopping.

### Funnel diagnosis

Use when the user provides several funnel metrics or a dataset.

1. Normalize definitions, time window, cohort, denominator, and channel segmentation.
2. Calculate comparable stage rates when raw counts are available.
3. Route through the funnel and identify the earliest material break.
4. Cross-check downstream signals without treating them as independent proof.
5. Produce the diagnosis report.

### Pre-launch readiness

Use when the product has not launched or has no meaningful user cohort yet.

Do not pretend to diagnose conversion performance. Inspect whether the product is ready to learn after launch: promise, first-use path, candidate Aha Moment, pricing comprehension, trust, event instrumentation, and cohort definitions. Read [references/prelaunch.md](references/prelaunch.md) and produce a readiness report with the three highest launch risks and a first-week measurement plan.

### Focused audit

Use when the user explicitly asks about one stage such as onboarding or pricing.

Audit that stage directly, but briefly test whether an upstream issue could invalidate the work. Do not force a complete funnel audit when the focused question is already well scoped.

## Load only the references needed

- For intake, metric definitions, cohort hygiene, and benchmark use, read [references/intake-and-metrics.md](references/intake-and-metrics.md).
- For a product without meaningful user data, read [references/prelaunch.md](references/prelaunch.md).
- For stage ordering and bottleneck selection, read [references/funnel-routing.md](references/funnel-routing.md).
- For acquisition and audience-quality symptoms, read [references/traffic-quality.md](references/traffic-quality.md).
- For homepage or landing-page conversion, read [references/landing-page.md](references/landing-page.md).
- For onboarding, Aha Moment, time-to-value, and activation, read [references/activation.md](references/activation.md).
- For upgrade motivation, trial design, paywalls, and checkout, read [references/trial-to-paid.md](references/trial-to-paid.md).
- For packaging and pricing-page clarity, read [references/pricing.md](references/pricing.md).
- For churn, cohort retention, and expansion, read [references/retention.md](references/retention.md).
- Before finalizing a diagnosis, read [references/report-template.md](references/report-template.md).

Do not load every specialist reference by default. Start with intake and routing, then open only the suspected bottleneck reference and any directly adjacent stage needed to test causality.

## Make the core judgment

For each relevant stage, assign one status:

- `Supported`: evidence is sufficiently consistent for an actionable conclusion.
- `Probable`: several signals align, but a decision-changing fact is missing.
- `Unknown`: the available evidence does not support a stage judgment.
- `Not primary`: a weakness may exist, but an earlier bottleneck should be addressed first.

Choose one primary bottleneck unless the evidence shows two independent failures. Explain why it comes before the alternatives.

When evidence conflicts, prefer segmented cohort behavior over blended averages, user behavior over stated preference, and completed outcomes over clicks or page views.

## Recommend experiments

Return no more than three priority experiments. Each experiment must include:

- hypothesis;
- smallest concrete change;
- target cohort;
- primary metric;
- guardrail metric;
- observation window or sample requirement;
- decision rule for keep, iterate, or stop.

Do not rank an experiment highly merely because it is easy. Prioritize its ability to test the primary diagnosis with reasonable effort and reversible risk.

## Finish well

Use the structure in [references/report-template.md](references/report-template.md). Keep the report understandable to a founder who is not an analytics specialist.

End with one immediate action the user can take today. Include the deeper-diagnosis handoff only when the next decision genuinely requires private analytics, recordings, interviews, full product access, or sustained experiment design. Never withhold a useful conclusion to force the handoff.
