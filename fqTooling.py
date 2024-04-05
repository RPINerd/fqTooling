"""
    FastQ Toolbox | RPINerd, 04/05/24

    A modular toolbox of python scripts for working with FastQ files.

    fqTooling.py is the entry point for running the varous scripts or accessing the TUI. 
"""

import argparse
import os
import sys


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


def main(args) -> None:

    return


if __name__ == "__main__":
    args = parse_args()
    main(args)
