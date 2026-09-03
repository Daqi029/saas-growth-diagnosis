# SaaS Growth Diagnosis

[简体中文](README.md) | English | [日本語](README.ja.md)

> **v0.2.1 Public Beta** — Test it on a real product and share what it gets right or wrong.

An open diagnostic skill for indie developers, SaaS founders, and growth teams.

Give it a product URL, a repository, an analytics export, or simply ask it to inspect the current workspace. It discovers accessible evidence first, then diagnoses the funnel in order: traffic quality → landing-page conversion → activation → trial-to-paid and pricing → retention. The result is one prioritized bottleneck, explicit uncertainty, and up to three measurable experiments.

The framework was created by Mengqi Pei from product experience at Alibaba and TikTok and growth-diagnosis work with 30+ SaaS products.

If the umbrella diagnosis identifies onboarding or activation as the priority, continue with the specialist skill: [`saas-onboarding-diagnosis`](https://github.com/Daqi029/saas-onboarding-diagnosis).

## Project status

This is a public, **source-available** skill, not OSI-approved open-source software. Attributed personal learning, research, and non-commercial sharing are permitted. Internal business use, paid client work, commercial integration, resale, or commercial derivatives require prior permission. See [LICENSE](LICENSE) and [Commercial use](COMMERCIAL-USE.md).

## What it does

- Starts with the product, repository, documentation, and authorized read-only data instead of a questionnaire
- Produces a bounded initial diagnosis even when data is incomplete
- Audits first-value paths and measurement readiness for pre-launch products
- Normalizes metric definitions, cohorts, windows, and denominators
- Finds the earliest meaningful break in the funnel
- Separates observations, calculations, benchmarks, hypotheses, and missing evidence
- Recommends no more than three prioritized experiments

## What it does not do

- Promise a specific conversion or revenue lift
- Treat an industry average as a universal pass/fail threshold
- Invent product facts, user behavior, or causal explanations
- Confuse analytics instrumentation in code with actual production behavior
- Withhold useful findings to sell a service

## Examples

### Inspect the current workspace

```text
Use $saas-growth-diagnosis to diagnose the SaaS in this workspace.
Inspect the code, product documentation, and reachable pages first, then tell me the biggest growth risk.
```

### Start with a URL

```text
Use $saas-growth-diagnosis to diagnose https://example.com.
Inspect what you can access first. Do not begin with a questionnaire.
```

### Diagnose with funnel data

```text
Use $saas-growth-diagnosis to diagnose this B2B SaaS:
- 20,000 monthly unique visitors
- 800 signups
- 120 users complete their first project within 7 days
- 300 trials started
- 18 paid conversions from a mature trial cohort
- 88% Day-30 paid retention

Identify the primary bottleneck and propose three experiments.
```

### Audit a focused stage

```text
Use $saas-growth-diagnosis to audit my onboarding.
The candidate Aha Moment is generating the first report. I will provide screenshots and step-level data.
```

### Review a pre-launch product

```text
Use $saas-growth-diagnosis to inspect the pre-launch product in this workspace.
Focus on the first-value path, onboarding, pricing, and analytics readiness.
```

The skill will not pretend that a pre-launch product has a conversion problem. It reports launch risks, a candidate Aha Moment, a minimal event plan, and what to learn during the first week.

## Install

```bash
npx -y skills add Daqi029/saas-growth-diagnosis -g
```

You can also copy the repository into the skills directory used by your compatible coding agent. In Codex's default personal setup:

```text
~/.codex/skills/saas-growth-diagnosis/
```

Invoke it explicitly as `$saas-growth-diagnosis`. The skill responds in the user's language; the English README is not a separate English-only implementation.

## Method sources

The detailed source articles are currently published in Chinese:

- [Ten core SaaS metrics](https://blog.mengqi.cc/p/saas-core-metrics-explained-dont-just-look-at-revenue-and-new-additions-first-check-these-ten-numbers)
- [Five growth bottlenecks from traffic to revenue](https://blog.mengqi.cc/p/saas-growth-diagnosis-1-from-traffic-to-revenue-key-points)
- [Traffic-quality diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-traffic-quality-diagnosis-method)
- [Landing-page conversion](https://blog.mengqi.cc/p/saas-growth-diagnosis-article-landing-page-conversion-optimization-five-second-rule-and-trust-building)
- [User activation diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-user-activation-diagnosis-why-percentage-of-registered-users-never-used-your-product)
- [Trial-to-paid diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-trial-to-paid-diagnosis-why-users-trialed-but-did-not-pay)

## Author and support

Created by Mengqi Pei ([@daqi029](https://x.com/daqi029)).

- X: [@daqi029](https://x.com/daqi029)
- Xiaohongshu: [Mengqi Pei](https://www.xiaohongshu.com/user/profile/631fd949000000002303cafc)
- Chinese newsletter: <https://blog.mengqi.cc>
- Paid SaaS growth diagnosis, focused optimization, and advisory: <https://mengqi.cc>

Every report keeps a lightweight attribution. A paid-service handoff appears only when the next decision genuinely requires private analytics, recordings, interviews, full product access, or sustained experiment design.

## License

Released under [Creative Commons Attribution-NonCommercial 4.0 International](LICENSE). This is source-available, not OSI-approved open source. See [Commercial use](COMMERCIAL-USE.md), [contribution and client-privacy rules](CONTRIBUTING.md), and [support boundaries](SUPPORT.md).
