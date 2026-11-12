# Finding a name · IS218 Creative Project Plan

[Published programming research](https://is218-directory-search-exploration.akindemuyi18.chatgpt.site) · [Site source](dist/index.html) · [Repository](https://github.com/oa356/is218-class) · [Portfolio Plan site](https://is218-ai-career-research.akindemuyi18.chatgpt.site) · [Portfolio record](../career-research/README.md)

## Plan

**Question** · Can typo-tolerant search help first-year commuters find campus services from half-remembered names while keeping correctly spelled searches predictable?

**Audience** · First-year commuter students finding a service between classes. A search-first screen suits someone with a task in mind. A category-first screen would help an orientation visitor explore what exists. Start with search and show categories on results. The small catalog and the need for typo assistance are assumptions.

**Dream** · A commuter can find the right campus service from an incomplete name and return to it later.

**Working promise** · Register and sign in, search a small campus service catalog, bookmark one result, return to a private dashboard, change a display name and password, then sign out.

| Concept | Bounded interaction and result | Tradeoff |
| --- | --- | --- |
| Campus resource finder | Search services by name or category. Save a unique bookmark and see the count and recent links. First screen starts with a search box and result list. | Builds on the tested lookup. Similar names can create misleading suggestions. |
| Between-class study planner | Select a subject and one of three preset durations. Save a plan and see recent plans and total planned minutes. First screen starts with a subject and duration form. | Simpler rules. It would test time planning and need its own evidence about preferred durations. |

**Choice** · Build the resource finder. The current browser demo uses four fictional names to test search. The application will start with a small synthetic service catalog.

## Five stories and expected results

| Story | Expected check |
| --- | --- |
| As a new student, I can register and return. | Sign up and sign in. A duplicate username or wrong password produces an error. |
| As a commuter, I can find and bookmark a service. | A valid name or category finds the expected resource. Blank queries show guidance, unknown resource IDs are rejected, and two saves leave one bookmark. |
| As a returning student, I can reopen my saved links. | A new dashboard has an empty state. Count and recent bookmarks survive a new session and restart. A second account cannot read or change the first account's records. |
| As a signed-in student, I can maintain my account. | Display name changes persist. Password change requires the current password, leaves the current session active, invalidates the other session, and rejects the old password at sign-in. |
| As a student leaving a shared device, I can sign out. | The old session cannot open the dashboard or save a bookmark. |

## Architecture and stack

`Browser and Django templates → Django forms, views and authentication → SQLite through the Django ORM`

Python with Django 5.2 handles form validation, authentication and sessions. A small JavaScript module searches the public catalog in the browser. For a save, the server validates the resource ID, requires a signed-in session and CSRF protection, and takes the owner from that session. The database stores users, resources and timestamped bookmarks with a unique owner/resource pair. Dashboard reads filter by owner. Account edits apply to the signed-in account. Use Django's test client with synthetic users, then verify the complete journey in a browser.

## Research and experiment

Original sources checked November 12, 2026.

- ECMAScript defines literal substring search and NFC normalization. Use those operations for a deterministic baseline. [ECMAScript includes](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.includes) · [ECMAScript normalize](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.normalize)
- Fuse.js documents approximate matches and scores. Test the interpretation that ranked suggestions can recover typos in this small catalog. [Fuse.js docs](https://www.fusejs.io/)
- Django documents password hashing and session invalidation, along with CSRF protection for internal forms. Apply those patterns and independently test two-user isolation. [Authentication](https://docs.djangoproject.com/en/5.2/topics/auth/default/) · [CSRF](https://docs.djangoproject.com/en/5.2/howto/csrf/)
- SQLite is designed for local application storage and has tradeoffs with concurrent writers. Choose it for the small local app. [SQLite use cases](https://www.sqlite.org/whentouse.html)

**Experiment** · Compare literal search with a fallback labeled “Possible matches.” Give both 12 labeled queries against the same synthetic catalog, including similar names. Expect at least four of five typos to place the intended result in the top three, all four literal queries to keep their result order, and at most one of three unrelated queries to get suggestions. Stop after 45 minutes if the criteria fail or the rankings are unclear. Keep literal search with a prompt to try a shorter query.

**Pattern trial** · Compare an inline conditional with separate literal and fuzzy search functions that return the same result shape. Run the same cases on each. Keep the structure that makes the results and fallback easiest to trace.

AI helped draft the alternatives, fixture and planned checks. The source claims were checked against original documentation. Independently specified queries were used to check the baseline. Next, record the chosen threshold and actual search errors before deciding whether to add suggestions.

## Verification

| Status | Check and result |
| --- | --- |
| Observed · November 11 | Five local baseline cases matched expectations. Uppercase with spaces found Ben Park, `Chen` found Avery Chen, the decomposed accent found Amélie Laurent, and `Jodran` and `ZZZ` returned no match. The published demo also returned Avery Chen for `Chen`. [Baseline evidence](https://is218-directory-search-exploration.akindemuyi18.chatgpt.site/#checks) |
| Observed · November 12 | Reran the five baseline form checks and confirmed a blank query prompts for a name. All six passed. All seven local navigation links resolved, and the plan contains five stories. |
| Observed on the live site · November 12 | The browser returned Avery Chen for `Chen`, showed no match for `Jodran`, and prompted for a name on blank input. Followed the links between the Creative Project and Portfolio sites in both directions. [Live baseline](https://is218-directory-search-exploration.akindemuyi18.chatgpt.site/#checks) |
| Planned | Compare fuzzy suggestions and the two search structures on the 12 labeled queries. |
| Planned | Implement and test the account journey, server validation, duplicate saves, ownership, restart persistence and session behavior. |
| Pending | Partner opens the Fuse.js source, tries the two baseline queries, explains the fallback choice and identifies an assumption. Record the observation, the owner decision and any linked change, then ask the partner to retry. [Open peer review issue](https://github.com/oa356/is218-class/issues/2) |

[Course project brief](https://github.com/kaw393939/is218-studio/blob/main/docs/projects/individual.md)
