# Bench & Bolt · Group Customer Studio plan

[Customer notes](customer-kit/CUSTOMER-NOTES.md) · [Prepared scenario](https://github.com/kaw393939/is218-studio/blob/main/docs/public/kits/fde-customer/scenarios/repair-shop.md) · [Course group brief](https://github.com/kaw393939/is218-studio/blob/main/docs/projects/group.md)

**Review 1 status** · Proposed scope. Confirm the customer, stories and work owners with the team. Implementation and real peer review are pending.

## Customer and scope

The prepared customer is Maya Chen, owner of a fictional bike-repair shop. The coordinator needs one place to record walk-in inquiries, review them and show what the shop has decided.

| Scope | Workflow | Tradeoff |
| --- | --- | --- |
| A · Staff intake | A trusted coordinator logs a walk-in inquiry, finds it in the queue and records the decision. | One local interface and one operating role let us focus on correct status and persistence. |
| B · Rider intake | Riders submit inquiries through a separate form. The coordinator reviews the same queue. | Riders can enter their own requests. The public form and private queue add a second surface and require server-side coordinator access controls. |

**Proposed choice** · A, a local staff-only app. One coordinator records a repair inquiry, gives the rider a pending reference and updates the same stored record. Synthetic fixtures only. Online booking, quotes, payments, inventory and outbound messages are outside the planned workflow.

**Workflow** · Walk-in details → validate and save inquiry → Pending review receipt → coordinator queue → decision → matching queue and detail status.

## Stories and expected checks

| Story | Expected result |
| --- | --- |
| **1. Log a walk-in.** As coordinator, I can enter a city bike with “Rear brake squeals” and preferred day “Tuesday.” | Save one inquiry and show its generated ID with **Pending review**. Blank or overlong problems, unsupported bike types and overlong preferred-day text create no row. Tuesday is a preference. |
| **2. Find the same inquiry.** As coordinator, I can locate it in the queue and open its details. | Queue and detail use the same ID, submitted values and stored status. Restart using the same database and find the same record in the same creation order. |
| **3. Record the decision.** As coordinator, I can accept or decline a pending inquiry and complete an accepted one. | Pending → Accepted → Completed and Pending → Declined work. Pending → Completed and terminal edits are rejected by the server without a stored change. |
| **4. Explain the outcome.** As coordinator, I can tell the rider what happens next using their inquiry reference. | The receipt/detail and queue agree after refresh. A pending request awaits review, an accepted request records the shop's decision to take the job, and completed records finished work. The preferred day stays labeled as a request throughout. |

## Data and status rules

Store one row per inquiry in SQLite. Fields are a generated ID, synthetic rider label, bike type (`city`, `road`, `other`), trimmed problem text (1–240 nonblank characters), optional preferred day (up to 40 characters), status and creation order. Validate these on the server. Use the same stored row in the queue and detail. A generated ID and status come from the server.

| From | Allowed next status | Meaning |
| --- | --- | --- |
| New inquiry | Pending review | Recorded and awaiting a shop decision. |
| Pending review | Accepted or Declined | The shop agrees to take the job or declines it. Accepted carries no appointment or charge. |
| Accepted | Completed | The coordinator records finished work. |
| Completed or Declined | None | Terminal for this workflow. |

## Architecture and pattern

`Browser intake / queue / detail → Flask routes → validation and transition rules → SQLite`

**Proposed stack** · Python, Flask templates and SQLite. Flask handles intake and decision requests. A validation function checks inputs. The transition rule guards writes against the current stored status. SQLite keeps the inquiry across reload and restart. Use Flask's test client and a temporary database for implementation checks.

For the first slice, compare an inline conditional with a status-to-allowed-next-status table. Run the same allowed and rejected pairs against both and retain the version a teammate can inspect most readily. If the deployment scope becomes public, coordinator operations and queue access will need server-side sign-in and authorization.

## Work and cross-review

These two slices are proposed for a pair. Assign them by name together. If there is a third member, split detail/receipt and restart verification into a third slice and rebalance the work.

| Proposed owner | Design and development | QA and cross-review |
| --- | --- | --- |
| Intake owner · name pending | Sketch the intake and receipt, implement input validation and record creation, and render errors and the pending reference. | Test valid and rejected intake. Review the other owner's queue and try an illegal transition. |
| Queue owner · name pending | Sketch queue and status controls, implement saved reads and status changes, and handle terminal states. | Test valid and rejected transitions and restart persistence. Review the other owner's intake with valid, blank and unsupported inputs. |
| Both | Agree on the field contract, state labels and database interface. Record decisions in this spec. | Trace a saved request across the two slices and run one classmate walkthrough. |

## Checks and review

- **Checked for Plan** · Compared both prepared scopes, all four stories, the field constraints, and the allowed transitions against the official scenario. [Scenario source](https://github.com/kaw393939/is218-studio/blob/main/docs/public/kits/fde-customer/scenarios/repair-shop.md)
- **Planned implementation checks** · Valid intake and exact receipt values, no write on invalid intake, allowed and rejected transitions, queue/detail agreement, and persistence after restart. Record actual commands and results here when run.
- **Pending team and peer checks** · Confirm names and owners. Ask a classmate to use the proposed Tuesday walk-in and explain what the Pending review receipt promises, then trace where the coordinator would find it. Record the first confusing step, the team's decision, a linked change and the classmate's retry. 

**Initial contribution** · The proposed scope comparison, workflow rules and acceptance checks were drafted with AI assistance. Record the team's decisions and each member's actual contribution as work proceeds.
