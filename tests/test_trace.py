"""Example test for showme.trace."""

from typing import Any

import showme


@showme.trace
def fname(a: Any, b: Any) -> None:  # type:ignore[misc]
    """Docstring for fname."""


if __name__ == "__main__":
    fname("navdeep", "gill")
