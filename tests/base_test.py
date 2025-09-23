import pytest


@pytest.mark.usefixtures("soft_assert")
class BaseTest:
    """Base test class to provide shared fixtures like soft_assert"""
    pass
