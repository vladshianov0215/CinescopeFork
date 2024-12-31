import pytest

@pytest.fixture
def base_url():
    return "https://auth.dev-cinescope.store"

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
