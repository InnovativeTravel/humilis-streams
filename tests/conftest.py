"""Global conftest."""
import pytest
from collections import namedtuple


@pytest.fixture(scope="session")
def settings():
    """Global test settings."""
    Settings = namedtuple('Settings', 'stage environment_path layer_name')
    return Settings(stage="TEST",
                    environment_path="streams.yaml",
                    layer_name="streams")
