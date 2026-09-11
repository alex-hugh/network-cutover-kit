  #!/usr/bin/env python3
"""Test TCP connectivity to one or more services.

Examples:
  python tools/tcp_probe.py --target example.com:443
  python tools/tcp_probe.py --target dns.google:53 --target 1.1.1.1:443
"""

from __future__ import annotations

import argparse
import socket
import sys
import time
from dataclasses import dataclass


@dataclass
class ProbeResult:
    target: str
    success: bool
    elapsed_ms: float | None
    detail: str


def parse_target(value: str) -> tuple[str, int]:
    """Parse host:port or [ipv6-address]:port."""
    if value.startswith("["):
        host, separator, port_text = value[1:].partition("]:")
        if not separator:
            raise argparse.ArgumentTypeError(
                "IPv6 targets must use the format [address]:port"
            )
    else:
        host, separator, port_text = value.rpartition(":")

    if not separator or not host or not port_text:
        raise argparse.ArgumentTypeError(
            "Target must use host:port, for example firewall.example:443"
        )

    try:
        port = int(port_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Port must be a number") from exc

    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError("Port must be between 1 and 65535")

    return host, port


def probe(target: str, timeout: float) -> ProbeResult:
    host, port = parse_target(target)
    started = time.perf_counter()

    try:
        with socket.create_connection((host, port), timeout=timeout):
            elapsed_ms = (time.perf_counter() - started) * 1000
            return ProbeResult(target, True, elapsed_ms, "TCP connection established")
    except OSError as exc:
        elapsed_ms = (time.perf_counter() - started) * 1000
        return ProbeResult(target, False, elapsed_ms, str(exc))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test TCP connectivity to one or more network services."
    )
    parser.add_argument(
        "--target",
        action="append",
        required=True,
        help="Target in host:port format. Repeat for multiple targets.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Connection timeout in seconds (default: 5).",
    )
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")

    print(f"{'TARGET':<35} {'RESULT':<8} {'TIME':>9}  DETAIL")
    print("-" * 90)

    failures = 0
    for target in args.target:
        try:
            result = probe(target, args.timeout)
        except argparse.ArgumentTypeError as exc:
            result = ProbeResult(target, False, None, str(exc))

        status = "PASS" if result.success else "FAIL"
        elapsed = f"{result.elapsed_ms:.1f} ms" if result.elapsed_ms else "-"
        print(f"{result.target:<35} {status:<8} {elapsed:>9}  {result.detail}")

        if not result.success:
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
