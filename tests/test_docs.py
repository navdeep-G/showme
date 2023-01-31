"""Example test for showme.docs."""

"""

>>> test()
sample docstring for test

"""


import showme


@showme.docs
def test() -> None:
    """Sample docstring for test."""


if __name__ == "__main__":
    test()
