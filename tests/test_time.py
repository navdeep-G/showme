"""Example test for showme.time."""
import showme


@showme.time
def test() -> None:
    """Docstring for test."""
    for i in range(1000):
        i**i
    return 1


if __name__ == "__main__":
    test()
