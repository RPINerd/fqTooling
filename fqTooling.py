"""
    FastQ Toolbox | RPINerd, 04/05/24

    A modular toolbox of python scripts for working with FastQ files.

    fqTooling.py is the entry point for accessing the TUI and launching the various tools.

"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, ContentSwitcher, DirectoryTree, Footer, Header, Input, Select

from tool_widgets import TOOLS, Downsample, FastQC


class Toolbox(App):
    """
    FastQ Toolbox
    """

    # Options for the footer
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    # CSS Styling Reference
    CSS_PATH = "fqTooling.tcss"

    def compose(self) -> ComposeResult:
        """
        Compose the FastQ Toolbox
        """

        with VerticalScroll(id="tool_tabs"):
            yield Button("FastQC", id="fastqc")
            yield Button("Downsample", id="downsample")
            # for tool in TOOLS.keys():
            #     yield Button(tool, id=tool.lower().replace(" ", "_"))

        with Container(id="tool_content"):
            with ContentSwitcher(initial="fastqc"):
                yield FastQC(id="fastqc")
                yield Downsample(id="downsample")

    def on_mount(self) -> None:
        """
        Called when the app is mounted
        """
        pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle the button being clicked
        """
        self.query_one(ContentSwitcher).current = event.button.id


if __name__ == "__main__":
    Toolbox().run()
