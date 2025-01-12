#!/usr/bin/env python
# ruff: noqa
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

        raise

    # This allows easy placement of apps within the interior
    # dj_template directory.
    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "dj_template"))

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
