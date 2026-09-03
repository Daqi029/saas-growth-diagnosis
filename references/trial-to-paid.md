# Trial-to-paid diagnosis

Audit three layers in order: paid motivation → upgrade timing → purchase completion.

## Layer 1: paid motivation

First confirm that the user experienced the core value. If not, route back to activation.

Then ask:

- What recurring job or dependency exists after activation?
- What limitation, scale threshold, collaboration need, quality level, or risk reduction makes the paid plan valuable?
- Does the free experience solve enough to prove value without removing every reason to upgrade?
- Can the user explain what changes after paying?
- Is the paid value tied to actual usage and job progress rather than an arbitrary lock?

Avoid recommending artificial frustration, dark patterns, or degradation of already-earned user data.

## Layer 2: upgrade timing

Prefer behavior-driven prompts after a value or dependency event over a calendar-only prompt.

Evidence to inspect:

- day and usage state when successful customers upgrade;
- activity peak and drop-off during the trial;
- events immediately before upgrade;
- prompt frequency and dismissal behavior;
- conversion by trial length and acquisition cohort.

Common failures:

- asking for payment before the user experiences value;
- waiting until the user has already stopped using the product;
- showing the same prompt on every login;
- prompting on time elapsed rather than value-bearing behavior;
- offering a discount before clarifying paid value.

## Layer 3: purchase completion

If users select a plan or enter checkout but do not pay, inspect:

- plan-selection clarity;
- number of checkout steps and unnecessary fields;
- supported payment methods for the target market;
- tax, invoice, currency, and company-purchase needs;
- security, refund, cancellation, and support reassurance;
- errors, latency, mobile behavior, and failed-payment recovery.

Directional source signals:

- checkout completion below 70% → purchase friction is worth investigating;
- a step losing more than 20% of entrants → inspect that step first;
- more than three essential purchase steps → test whether information can be deferred.

These are heuristics, not laws. High-consideration or compliance-heavy purchases may legitimately need more steps.

## Interpreting trial-to-paid rates

The source series proposes this rough routing for time-limited trials:

- below 5%: investigate value experience and paid motivation first;
- 5–8%: investigate upgrade timing;
- above 8%: look for purchase-flow improvements after confirming no earlier break.

Do not apply this routing blindly to freemium, reverse-trial, enterprise, low-volume, or sales-assisted products.

## Candidate experiments

- Trigger the upgrade message after a verified value event rather than on day N.
- Rewrite the upgrade moment around the job unlocked, not a list of premium features.
- Introduce one honest usage or collaboration threshold that follows value.
- Reduce plan-selection ambiguity and defer nonessential checkout fields.
- Add a relevant payment method or failed-payment recovery for a proven lost cohort.

## Source

- Mengqi Pei, [Trial-to-paid diagnosis](https://blog.mengqi.cc/p/saas-growth-diagnosis-trial-to-paid-diagnosis-why-users-trialed-but-did-not-pay)
