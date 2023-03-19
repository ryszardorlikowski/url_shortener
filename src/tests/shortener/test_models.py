import pytest
from django.conf import settings
from django.db import IntegrityError

from shortener.factories import ShortLinkFactory


@pytest.fixture
def test_url() -> str:
    return 'http://test.com/test'


@pytest.mark.django_db
def test_create_link_object(test_url):
    """
    Test checking the correct creation of a link object
    """
    short_link = ShortLinkFactory(url=test_url)

    assert short_link.url == test_url
    assert type(short_link.code) == str
    assert len(short_link.code) == settings.SHORT_URL_CODE_LENGTH


@pytest.mark.django_db
def test_database_throws_exception_on_non_unique_code_field(test_url):
    """
    Test to check if the database raise an exception when trying to save a record with a non-unique code field.
    """
    ShortLinkFactory(url=test_url, code='test')

    with pytest.raises(IntegrityError):
        ShortLinkFactory(url=test_url, code='test')
