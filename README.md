# Network Cutover Kit

Open-source templates and validation tools for planning, delivering, and evidencing safe network and firewall cutovers.

Network changes often fail not because the configuration is difficult, but because the preparation, test plan, rollback path, and evidence are inconsistent. This project provides a practical, vendor-neutral starting point for engineers delivering infrastructure changes.

## What this project will include

* Cutover runbook / MOP templates
* Pre-change readiness and risk checks
* Implementation and rollback checklists
* Test and acceptance evidence templates
* Python validation tools for common network checks
* Example workflows for switch, firewall, WAN, and wireless changes

## Intended users

Network engineers, infrastructure teams, MSPs, and technical project leads carrying out planned production changes.

## Principles

* Vendor-neutral where possible
* Clear rollback before implementation begins
* Evidence-led testing and acceptance
* Safe defaults and reviewable changes
* Useful in real-world, time-constrained change windows

## Project status

Early-stage. Initial templates and validation tooling are being developed and reviewed.

## Contributing

Issues, feedback, improvements, and examples of practical cutover workflows are welcome.

## Licence

Released under the [MIT License](LICENSE).

## Quick start

No third-party Python packages are required.

Test one or more TCP services:

```bash
python tools/tcp_probe.py --target example.com:443
python tools/tcp_probe.py --target 1.1.1.1:443 --target dns.google:53
