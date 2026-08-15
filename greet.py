#!/usr/bin/env python3
"""Tiny CLI greeting tool (issue #23).

Prints `Hello, <name>!` to stdout and exits 0.

    python3 greet.py [--name NAME] [--shout]

--name NAME  personalises the greeting (default: world; value used verbatim)
--shout      uppercases the entire greeting line

Invalid arguments (unknown option, missing --name value) print a usage
message to stderr and exit with code 2 (standard argparse behaviour).

See specs/001-cli-greeting-tool/contracts/cli.md for the full contract.
"""

import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Print a friendly greeting.",
    )
    parser.add_argument(
        "--name",
        default="world",
        help="recipient of the greeting (default: %(default)s)",
    )
    parser.add_argument(
        "--shout",
        action="store_true",
        help="uppercase the entire greeting",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    greeting = f"Hello, {args.name}!"
    if args.shout:
        greeting = greeting.upper()
    print(greeting)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
