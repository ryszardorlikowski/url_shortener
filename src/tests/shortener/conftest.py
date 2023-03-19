import pytest


@pytest.fixture(scope='session')
def test_url() -> str:
    return 'http://test.com/test'
