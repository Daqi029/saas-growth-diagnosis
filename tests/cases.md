# Behavioral test cases

These cases test observable behavior. They are not content templates.

## Case 1: activation is the earliest break

Input:

> B2B project-management SaaS, $29/month, 14-day trial. Monthly visitors 20,000; signups 800; 120 create a first real project within 7 days; 300 start a trial; 18 of a matured 300-user trial cohort pay. Paid Day-30 retention is 88%. Diagnose the biggest bottleneck.

Expected behavior:

- calculates signup rate as 4%, activation as 15%, and trial-to-paid as 6%;
- identifies activation as the earliest supported bottleneck rather than jumping to payment;
- questions why trial starters exceed activated users or asks whether cohort and event definitions differ;
- recommends activation experiments before discounting or checkout work;
- labels benchmark comparisons as directional.

Critical failure:

- recommends increasing traffic or adding discounts as the first move.

## Case 2: traffic segmentation beats blended averages

Input:

> A developer SaaS has a 7% blended signup rate. Product Hunt users activate at 42% and pay at 11%; broad display-ad users activate at 5% and pay at 0.6%. Display ads produce 70% of signups. The founder wants to redesign the homepage because blended trial-to-paid is low.

Expected behavior:

- identifies traffic quality or source-message fit as the earliest primary issue;
- avoids calling the 7% signup rate universally healthy;
- recommends segment-level targeting or message experiments before a full redesign;
- preserves the possibility that the page needs a channel-specific variant.

Critical failure:

- treats all signups as equivalent and prioritizes checkout.

## Case 3: focused landing-page audit with little data

Input:

> Review my B2B SaaS landing page. The hero says “Reimagine intelligence for modern teams.” I have no analytics yet.

Expected behavior:

- gives a provisional comprehension diagnosis;
- inspects the supplied page if reachable before asking anything;
- proposes a five-second test and asks at most one high-leverage question if target user and job cannot be inferred;
- does not fabricate conversion rates or customer evidence;
- suggests a concrete hero hypothesis without pretending it is proven.

Critical failure:

- invents an expected conversion lift or writes fake social proof.

## Case 4: high-consideration enterprise boundary

Input:

> Enterprise compliance SaaS, annual contracts around $80,000, demo-led sales cycle of 90 days. Website visitor-to-form conversion is 0.9%. Is that below the SaaS benchmark, and should we switch to freemium?

Expected behavior:

- refuses a direct self-serve benchmark comparison;
- asks for qualified pipeline, meeting, opportunity, win-rate, and sales-cycle evidence;
- does not recommend freemium from website conversion alone;
- explains the missing decision evidence.

Critical failure:

- declares 0.9% unhealthy solely because it is below a 2–5% B2B range.

## Case 5: near-neighbor request outside scope

Input:

> Set up my Google Ads account, choose bids, write every ad, and launch the campaign.

Expected behavior:

- states that channel execution is outside this skill's diagnosis scope;
- offers to diagnose the target audience, promise, funnel measurement, and success criteria;
- does not claim to launch or mutate an advertising account.

Critical failure:

- pretends the skill includes channel execution.

## Case 6: retention requires a natural cadence

Input:

> A monthly accounting SaaS says Day-7 retention is only 8%, so the founder wants daily reminder emails. Most customers reconcile books once near month-end. Paid monthly customer churn is 2.5%.

Expected behavior:

- rejects Day-7 activity as sufficient proof of poor retention for a monthly job;
- asks for monthly cohort retention, successful reconciliation, revenue retention, and return behavior around month-end;
- does not recommend daily reminders without a value-bearing trigger;
- distinguishes usage cadence from customer churn.

Critical failure:

- calls retention broken solely from Day-7 activity and recommends generic notifications.

## Case 7: repository-first discovery

Input:

> Diagnose the SaaS in the current workspace. The product is already live. Do not make me fill out a data questionnaire.

Workspace evidence:

- README identifies a B2B AI reporting product;
- routes include signup, onboarding, report editor, pricing, and checkout;
- onboarding requires company profile, CRM integration, team invitation, and template choice before report generation;
- analytics events exist for signup and checkout, but not for first successful report;
- no production analytics export is accessible.

Expected behavior:

- inspects the repository and reports what was inspected before asking the user;
- identifies a probable pre-value setup risk and a measurement gap;
- clearly says code does not prove actual user behavior;
- does not ask the user to manually list information already visible in the repository;
- proceeds with a provisional diagnosis and one next action, even without production metrics.

Critical failure:

- starts by sending a funnel-data form or claims the repository proves the live activation rate.

## Case 8: pre-launch product

Input:

> This SaaS has not launched. Inspect the current repository and tell me whether it is ready.

Workspace evidence:

- public landing page and working signup flow;
- first screen after signup is an empty dashboard;
- the core result is generated only after a five-step integration flow;
- analytics records page views and signup, but no value event;
- pricing exists but has not been shown to users.

Expected behavior:

- enters pre-launch readiness instead of funnel-performance diagnosis;
- describes empty state and setup as risks or hypotheses, not proven conversion problems;
- proposes a candidate Aha Moment and minimum event plan;
- identifies what should be changed before launch and what should wait for real users;
- does not ask for nonexistent conversion or retention data.

Critical failure:

- compares nonexistent metrics with industry benchmarks or asks the founder to supply retention data.
## Case 9 — English URL-only diagnosis

**Request:** “Use `$saas-growth-diagnosis` to diagnose https://example.com. Inspect what you can access before asking me for data.”

**Expected behavior:**

- Inspect the public product experience before asking a question.
- Write the complete diagnosis in English, including headings, uncertainty labels, experiments, and attribution.
- Do not require the user to translate the Chinese README or complete a questionnaire.
- Treat any inaccessible behavioral data as missing evidence rather than inventing it.

## Case 10 — Japanese localized diagnosis

**Request:** 「`$saas-growth-diagnosis` を使って、この SaaS のオンボーディングを診断してください。まず URL とリポジトリを確認し、質問票は送らないでください。」

**Expected behavior:**

- Inspect the URL and repository first and answer in natural Japanese.
- Localize headings, explanations, uncertainty labels, experiment descriptions, and author attribution.
- Keep product names, event names, and URLs unchanged when translation would reduce precision.
- Ask at most one decision-changing question after discovery.
