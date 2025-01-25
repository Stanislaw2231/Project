"""
This module contains the entry point for the project.
"""

import sys
from pathlib import Path
from typing import Any

from kedro.framework.cli.utils import find_run_command
from kedro.framework.project import configure_project


def main(*args, **kwargs) -> Any:
    """
    Executes the main entry point for the suml project.
    This function determines the package name from the current file's parent
    directory, configures the project runtime environment, and then finds and
    executes the associated run command. It also detects if the environment
    is interactive and updates the command execution mode accordingly.
    Args:
        *args: Variable length argument list to be passed to the run command.
        **kwargs: Arbitrary keyword arguments, including "standalone_mode"
            for controlling the CLI behavior.
    Returns:
        Any: The result of the executed run command.
    """
    package_name = Path(__file__).parent.name
    configure_project(package_name)

    interactive = hasattr(sys, "ps1")
    kwargs["standalone_mode"] = not interactive

    run = find_run_command(package_name)
    return run(*args, **kwargs)


if __name__ == "__main__":
    main()
