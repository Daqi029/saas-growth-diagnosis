# Intake and metrics

Use this reference to normalize the user's evidence before comparing stages.

## Evidence priority

Use evidence in this order before asking the user to retrieve anything:

1. Current conversation, supplied files, screenshots, and explicit product URL.
2. Current workspace and accessible repository.
3. Public product, pricing, documentation, and onboarding surfaces.
4. Existing local analytics exports, reports, or connected read-only data sources the user has already placed in scope.
5. One decision-changing question to the user when the answer cannot be discovered.

Do not make the user act as a courier between tools the agent can already access.

## What to inspect in an accessible repository

Keep discovery read-only. Prioritize:

- README, product specifications, architecture notes, and user stories;
- package manifests and app structure;
- routes and components for landing, signup, onboarding, empty states, upgrade, pricing, checkout, and cancellation;
- sample data, templates, default projects, checklists, and first-run feature flags;
- analytics SDKs, event names, identity logic, cohort definitions, and experiment flags;
- billing provider integration, plan identifiers, trials, limits, and paywall triggers;
- tests that reveal intended critical paths;
- public deployment and product documentation when linked.

Do not inspect or expose secret values, credentials, private customer records, or unrelated personal files. Environment-variable names may reveal integrations; their values are not needed for a first diagnosis.

Code shows intended behavior, not observed behavior. Label repo-derived conclusions as implementation evidence.

## What the agent ultimately needs to infer or obtain

The most decision-relevant fields are:

- product URL and one-sentence promise;
- target customer and primary job;
- B2B, B2C, enterprise, or mixed motion;
- acquisition channels and whether traffic is paid, organic, outbound, or referral;
- free trial, freemium, reverse trial, demo-led, or sales-led conversion;
- price, billing interval, and typical sales cycle;
- reporting window and cohort definition;
- visitors, signups, activated users, trial starters, paid customers, and retained customers;
- definition of activation or the current candidate Aha Moment;
- current business question and the decision the user is considering.

Many fields will remain unknown. Do not require a complete form. After discovery, ask one high-leverage question at a time only when the answer could change the primary bottleneck or next action. Otherwise state an assumption and proceed.

## What can and cannot be discovered automatically

| Evidence | Usually discoverable from code or public surfaces? | What it supports |
|---|---|---|
| Intended audience and promise | Often | Positioning hypothesis |
| Signup and onboarding steps | Often | Friction and readiness audit |
| Candidate Aha Moment | Sometimes | Activation hypothesis |
| Analytics event names | Sometimes | Measurement-readiness audit |
| Pricing and trial configuration | Often | Packaging and trigger audit |
| Actual traffic quality | Rarely from code | Requires behavioral or channel data |
| Actual conversion and retention | Rarely from code | Requires matured cohort data |
| User motivation and objections | Rarely | Requires interviews, feedback, or behavior |

When a connected analytics or data tool is available and clearly in scope, prefer a read-only query over asking the user to copy numbers. Explain the source and preserve privacy. If access is absent, propose the smallest export or query rather than a large data request.

## Metric definitions

Prefer counts and calculate rates when possible.

- Visitor-to-signup rate = new signups / eligible unique visitors.
- Activation rate = users who complete the defined value event / eligible new users.
- Time to value = elapsed time from signup or first eligible session to the value event.
- Trial-to-paid rate = paid customers from a matured trial cohort / eligible trial starters.
- Checkout completion = successful purchases / users who entered checkout or selected a plan; state the chosen denominator.
- Customer churn = customers lost during period / customers at start of period.
- Revenue churn = recurring revenue lost during period / recurring revenue at start of period.
- Retention for a cohort = cohort members active or paying at the chosen age / original eligible cohort.
- ARPU = recurring revenue / paying customers for the same period.
- CAC = attributable acquisition and sales cost / new paying customers.
- CPL or cost per signup = attributable acquisition cost / new signups.
- Simplified LTV = ARPU / monthly customer churn. Label this as a rough model and avoid it when churn is unstable or gross margin materially changes the result.
- NRR = (starting recurring revenue + expansion - contraction - churn) / starting recurring revenue.

## Cohort hygiene

Before interpreting a rate, check:

1. Is the numerator from the same eligible cohort as the denominator?
2. Has the cohort matured long enough to observe the outcome?
3. Are bots, employees, duplicate accounts, test traffic, and obvious spam excluded?
4. Are paid and organic channels blended despite different intent?
5. Are self-serve and sales-assisted customers blended?
6. Did price, onboarding, targeting, or instrumentation change inside the window?
7. Is the sample large enough that a few users dominate the rate?

If any answer is unclear, state the limitation. Do not create false precision.

## Directional benchmark ranges from the source series

Use these only to form hypotheses. Product type, price, channel, maturity, sales motion, geography, and metric definitions can make direct comparisons invalid.

| Metric | Directional context |
|---|---|
| Visitor → signup, B2B SaaS | 2–5% |
| Visitor → signup, B2C SaaS | 5–10% |
| Visitor → signup, freemium | 8–15% |
| Activation, B2B SaaS | 20–40% |
| Activation, B2C SaaS | 40–60% |
| Trial → paid, time-limited trial | 8–12% |
| Trial → paid, freemium | 2–5% |
| Trial → paid, reverse trial | 10–15% |
| Day-7 retention, B2B SaaS | 20–40% |
| Day-7 retention, B2C SaaS | 15–30% in the traffic article; broader contexts may differ |
| Monthly customer churn, B2B SaaS | 3–7% |
| Monthly customer churn, B2C SaaS | 5–10% |
| LTV/CAC | around 3 is commonly treated as healthy in the source series |

Never say a metric is healthy solely because it falls inside a range. Ask whether users reach durable value and whether unit economics support the business.

## Evidence labels

Label important claims in the report:

- `Fact`: directly supplied or visibly observed.
- `Calculation`: derived from stated numbers; show the formula.
- `Benchmark`: directional comparison with relevant caveats.
- `Hypothesis`: plausible explanation needing validation.
- `Missing`: evidence that could change the decision.

## Sources

- Mengqi Pei, [SaaS core metrics](https://blog.mengqi.cc/p/saas-core-metrics-explained-dont-just-look-at-revenue-and-new-additions-first-check-these-ten-numbers)
- Mengqi Pei, [Traffic quality diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-traffic-quality-diagnosis-method)
- Mengqi Pei, [User activation diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-user-activation-diagnosis-why-percentage-of-registered-users-never-used-your-product)
- Mengqi Pei, [Trial-to-paid diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-trial-to-paid-diagnosis-why-users-trialed-but-did-not-pay)
