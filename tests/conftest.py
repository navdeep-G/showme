"""Configuration for pytest to automatically collect types.

Thanks to Guilherme Salgado.
"""
from typing import Any, Iterator

import pytest
from pyannotate_runtime import collect_types


# pylint: disable=W0613
def pytest_collection_finish(*, session: Any) -> None:  # type:ignore[misc]
    """Handle the pytest collection finish hook: configure pyannotate.

    Explicitly delay importing `collect_types` until all tests have been
    collected.  This gives gevent a chance to monkey patch the world
    before importing pyannotate.
    """

    collect_types.init_types_collection()


# pylint: disable=W0613
@pytest.fixture(autouse=True)
def collect_types_fixture() -> Iterator:
    """Performs unknown activity."""

    collect_types.start()
    yield
    collect_types.stop()


# pylint: disable=W0613
def pytest_sessionfinish(  # type:ignore[misc]
    *,
    session: Any,
    exitstatus: Any,
) -> None:
    """Performs unknown activity."""
    collect_types.dump_stats("type_info.json")
