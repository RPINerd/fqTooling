"""
    These are the individual widgets that coordinate the input for each tool
"""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Button, Input

# Tools available in the toolbox
TOOLS = {
    "Base Content Filtering": "Description Here",
    "Degenerate Bases": "Description Here",
    "Diff": "Description Here",
    "Downsample": "Description Here",
    "FastQC": "Description Here",
    "Pairwise Alignment": "Description Here",
    "Read Pair Merging": "Description Here",
    "Regex Filtering": "Description Here",
    "Search": "Description Here",
    "Synchronize": "Description Here",
    "Unique": "Description Here",
    "Window Shopper": "Description Here",
}


class FastQC(Widget):
    """
    FastQC Tool

    This widget is responsible for collecting the input for the FastQC tool
    """

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter the path to the FastQ file")
        yield Button("Run")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle the button being clicked
        """
        self.log("Button clicked")


class Downsample(Widget):
    """
    Downsample Tool

    This widget is responsible for collecting the input for the Downsample tool
    """

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter the path to the FastQ file")
        yield Input(placeholder="Enter the path to the output file")
        yield Button("Run")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle the button being clicked
        """
        self.log("Button clicked")
