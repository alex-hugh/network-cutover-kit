# Pre-Cutover Readiness Checklist

Use this checklist before any planned production network, firewall, WAN, wireless, or security change.

**Change reference:**
**Service / site:**
**Planned start and finish:**
**Change owner:**
**Technical approver:**
**Rollback owner:**

---

## 1. Change control

* [ ] Scope is clear and agreed.
* [ ] Success criteria are measurable.
* [ ] Implementation steps are written, reviewed, and timed.
* [ ] A named technical owner is available throughout the change.
* [ ] Required customer, supplier, and internal contacts are available.
* [ ] Change approval has been obtained.
* [ ] Maintenance window and expected user impact have been communicated.

## 2. Backups and recovery

* [ ] Current configurations have been exported and stored securely.
* [ ] Device software and hardware details have been recorded.
* [ ] Existing topology and addressing information are available.
* [ ] Access details and break-glass credentials have been verified.
* [ ] A tested rollback plan exists.
* [ ] Rollback decision point and latest safe rollback time are agreed.

## 3. Connectivity and dependencies

* [ ] Management access path has been tested.
* [ ] Out-of-band or console access is available where practical.
* [ ] WAN circuits, handoffs, transceivers, patching, and port speeds are confirmed.
* [ ] VLANs, routing, IP addressing, NAT, VPN, DNS, DHCP, NTP, and authentication dependencies are understood.
* [ ] Upstream/downstream device owners have been identified.
* [ ] Monitoring, logging, and alerting implications have been reviewed.

## 4. Validation plan

* [ ] Pre-change baseline checks have been captured.
* [ ] Post-change tests are defined for every affected service.
* [ ] Test users, source locations, and test data are available.
* [ ] Monitoring dashboards and logs are open during the change.
* [ ] Acceptance criteria and evidence format are agreed.
* [ ] A communications plan exists for progress updates and incident escalation.

## 5. Go / no-go decision

The change may proceed only when all mandatory checks above are complete, or when an agreed exception and risk owner are recorded below.

**Go / no-go decision:**
**Decision time:**
**Approved by:**
**Exceptions / accepted risks:**

## 6. Post-change record

**Actual start:**
**Actual finish:**
**Validation completed by:**
**Outcome:**
**Follow-up actions:**
**Rollback required?** Yes / No

