# Portfolio verification

## Review 2 portfolio checks

November 19, 2026. These checks cover the source, the browser preview and the published draft. A human portfolio walkthrough and reviewer retry are pending.

| Check | Observed result |
| --- | --- |
| Find work from the research homepage | Opened **Portfolio draft**. Activating **Inspect project evidence** with Enter reached the work section. The three headings identified Campus Resource Finder, Residence Hall Maintenance and Bench & Bolt. |
| Compare the two presentations | Switched to **Field notebook** with Enter. Normalized visible main text matched between layouts. Browser geometry placed the three grid cards on the same row and the three notebook entries on separate rows. |
| Find résumé and profiles | The portfolio header exposed Résumé, GitHub and LinkedIn. From the notebook, **Read my résumé** opened Olumuyiwa Akinde's education, project experience and skills. Both layouts use the student's GitHub account and the LinkedIn profile URL from the source résumé. LinkedIn's public page blocked automated retrieval, so signed-out profile visibility is unverified. |
| Check the public résumé | The HTML résumé includes education, four linked projects, skills and both professional profiles. Print styles omit the site navigation. A physical printout is untested. |
| Check source navigation | All 28 local link and stylesheet references resolved across the three HTML pages, including 17 on-page links. |
| Check the analytics case against its evidence | Recounted 3,200 source rows and 3,199 distinct request IDs. The category table lists Plumbing 676, HVAC 508, Furniture 457 and Electrical 429. [Source data](https://github.com/oa356/residence-hall-operations-analysis/blob/main/data/raw/maintenance_requests_raw.csv) · [Chart data](https://github.com/oa356/residence-hall-operations-analysis/blob/main/reports/tables/category_summary.csv) |
| Distinguish individual and team work | The individual case links the implementation, tests and dated [app record](../../creative-exploration/README.md). The group case links the [team spec](../../group-customer-studio/SPEC.md) and labels implementation as pending. |
| Published reader path | Opened the public research home and followed **Portfolio draft**. [Evidence grid](https://is218-ai-career-research.akindemuyi18.chatgpt.site/portfolio?layout=grid) and [field notebook](https://is218-ai-career-research.akindemuyi18.chatgpt.site/portfolio?layout=notebook) displayed identical main text. The grid cards shared a row and the notebook entries stacked. From the live notebook, the [résumé](https://is218-ai-career-research.akindemuyi18.chatgpt.site/resume) opened and showed the print control and LinkedIn link. [Implementation commit](https://github.com/oa356/is218-class/commit/540012d5a995dce8970b826f97a8b0f18d348f91) |
| Human comparison | Pending. The reader task, decision and retry belong in [portfolio issue #1](https://github.com/oa356/is218-class/issues/1). |

## Review 1 plan checks

Checks recorded November 11, 2026.

| Check | Expected | Observed |
| --- | --- | --- |
| OpenAI role | The original description supports the customer-delivery summary and candidate profile. | Confirmed customer discovery through rollout, success measured by adoption and workflow impact, and a 5+ year candidate profile. New York hybrid and travel details were present. Posting date and deadline were unstated. [Employer description](https://openai.com/careers/forward-deployed-engineer-(fde)-nyc-new-york-city/) |
| Amazon role | The original description supports the applied-research summary, and the employer’s date refers to the same job ID. | Confirmed task and reward design, evaluation, Sunnyvale location and the two distinct experience requirements. Employer listings dated job 10595504 November 3, 2026. Deadline and work format were unstated. [Job description](https://amazon.jobs/en/jobs/10595504/applied-scientist-agi) · [Employer team listing](https://www.amazon.jobs/en-gb/business_categories/AGI) |
| Mayo Clinic role | The original description supports the healthcare workflow and eligibility summary. | Confirmed human review, model monitoring, two degree and experience routes, U.S. remote work and sponsorship restrictions. Posting date was April 29, 2026. Deadline was unstated. [Employer description](https://jobs.mayoclinic.org/job/rochester/ai-ml-engineer-revenue-cycle-automation-remote/33647/94534534048) |
| Site structure | Every local fragment link resolves to a unique element. The three employer cards link directly to employer descriptions. | Passed in source. 12 fragment links resolved across 13 unique IDs. All three employer links were present. The page requires no JavaScript. |
| Live sites and reciprocal links | Both research sites load publicly and each links to the other. | Both returned HTTP 200 without sign-in. Followed the Creative Project link and its return link in the browser. [Career research](https://is218-ai-career-research.akindemuyi18.chatgpt.site) · [Programming exploration](https://is218-directory-search-exploration.akindemuyi18.chatgpt.site) |
| Live programming demo | The published literal search returns Avery Chen when given the partial name Chen. | Passed in the browser. The fuzzy experiment remains planned. |
| Partner walkthrough | A partner finds Mayo Clinic’s human-review evidence, connects it to the portfolio decision, then identifies the expected handoff. | Pending. A peer has yet to report an observation. [Open walkthrough issue](https://github.com/oa356/is218-class/issues/1) |
| Partner retry | The same partner retries any accepted change on the updated site, then posts the observed result to the issue. | Pending. Keep the issue open until a successful retry is recorded. |
| Proposed prototype | Seven supported synthetic cases cite official sources and three unsupported cases route to human review. Compare with a manual lookup baseline. | Planned. Prototype check pending. |

The employer pages were readable on the check date. Application forms were inconclusive, so current acceptance is unconfirmed. Public project artifacts were consulted for the planned case studies. Their proposed case-study checks remain pending.
