"""Example test for showme.cputime."""

import showme


@showme.cputime
def test() -> int:
    """Docstring for test."""
    for i in range(1000):
        i**i
    return 1


if __name__ == "__main__":
    test()
