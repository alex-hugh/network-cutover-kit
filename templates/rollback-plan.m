# Network Cutover Rollback Plan

Use this template to define how a production change will be safely reversed if the agreed success criteria are not met.

- **Change reference:**
- **Service / site:**
- **Planned change window:**
- **Change owner:**
- **Rollback owner:**
- **Rollback decision authority:**

---

## 1. Rollback triggers

Rollback must be started if any of the following occur:

- [ ] Loss of a critical service outside the agreed impact.
- [ ] Validation tests fail and cannot be resolved within the agreed time.
- [ ] Management access is lost without a proven recovery path.
- [ ] Performance, stability, or security impact exceeds the agreed risk.
- [ ] The latest safe rollback time is reached.
- [ ] The rollback decision authority instructs it.

## 2. Prerequisites

Before starting the change, confirm:

- [ ] Current device configurations have been backed up and checked.
- [ ] Previous software images or configurations are available if needed.
- [ ] Required console, out-of-band, or remote access has been verified.
- [ ] Credentials and escalation contacts are available.
- [ ] Affected parties understand the rollback impact and communications plan.

## 3. Rollback steps

| Step | Action | Owner | Evidence / result |
|---|---|---|---|
| 1 | Announce rollback and record the decision time. |  |  |
| 2 | Stop the implementation at a safe point. |  |  |
| 3 | Restore the previous configuration or physical state. |  |  |
| 4 | Confirm device health, interfaces, routing, and management access. |  |  |
| 5 | Run service validation checks. |  |  |
| 6 | Confirm service restoration with stakeholders. |  |  |
| 7 | Send a final status update and record follow-up actions. |  |  |

## 4. Validation after rollback

- [ ] Management access restored.
- [ ] Core network connectivity restored.
- [ ] Routing, VPN, DNS, DHCP, and authentication checks completed where relevant.
- [ ] Monitoring and logging are reporting normally.
- [ ] Affected application or service owners confirm recovery.
- [ ] Incident/change record has been updated.

## 5. Record

- **Rollback started:**
- **Rollback completed:**
- **Outcome:**
- **Follow-up actions and root-cause investigation:**
