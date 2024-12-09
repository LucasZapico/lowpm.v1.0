from rich.console import Console
from rich.text import Text

console = Console()


def print_error(message: str, *err):
    """Prints an error message to the console."""
    tag = Text("ERROR:", style="bold red")
    console.print(tag, message, *err)


def print_info(message: str, *args):
    """Prints an info message to the console."""
    tag = Text("INFO:", style="bold cyan")
    console.print(tag, message, *args)


def print_warning(message: str, *args):
    """Prints an waring message to the console."""
    tag = Text("WARNING:", style="bold yellow")
    console.print(tag, message, *args)


def print_success(message: str, *args):
    """Prints an success message to the console."""
    tag = Text("SUCCESS:", style="bold green")
    console.print(tag, message, *args)