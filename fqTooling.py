"""
    FastQ Toolbox | RPINerd, 04/05/24

    A modular toolbox of python scripts for working with FastQ files.

    fqTooling.py is the entry point for accessing the TUI and launching the various tools.

"""

import rich


def inquire() -> str:
    """
    Present an interactive menu to the user that lists the available tools to choose from
    """

    questions = [
        {
            "type": "list",
            "name": "tool",
            "message": "What tool would you like to use?",
            "choices": [
                "Window Shopper",
                "FastQC Pipeline",
                "FastQ Trimmer",
                "FastQ Splitter",
                "FastQ Merger",
                "FastQ Stats",
                "FastQ QC",
                "FastQ Interleave",
                "FastQ Deinterleave",
                "FastQ Reverse Complement",
            ],
        }
    ]

    answers = prompt(questions)
    tool = answers["tool"]

    return tool


def main() -> None:
    """
    Main entry point for the FastQ Toolbox
    """

    tool = inquire()
    print(f"Selected tool: {tool}")


if __name__ == "__main__":
    print("Welcome to the FastQ Toolbox!")
    main()
