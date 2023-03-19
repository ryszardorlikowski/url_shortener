import pytest
from django.urls import reverse

from shortener.factories import ShortLinkFactory
from shortener.models import ShortLink


@pytest.mark.django_db
def test_create_short_url_view(api_client, test_url):
    """
    Test checking the correct creation of a shortened link
    """
    payload = {'url': test_url}
    response = api_client.post(reverse('create_short_link'), payload)

    assert response.status_code == 201
    short_link = ShortLink.objects.first()
    response_data = response.json()
    assert response_data['code'] == short_link.code
    assert response_data['url'] == test_url
    assert response_data['shortUrl'] == f"http://testserver/{short_link.code}"


@pytest.mark.django_db
def test_get_create_short_url_view(api_client, test_url):
    """
    Test checking the return of an existing link if it already exists
    """
    short_link = ShortLinkFactory(url=test_url)
    payload = {'url': short_link.url}

    response = api_client.post(reverse('create_short_link'), payload)

    response_data = response.json()
    assert response_data['code'] == short_link.code
    assert response_data['url'] == short_link.url
    assert response_data['shortUrl'] == f"http://testserver/{short_link.code}"


@pytest.mark.django_db
def test_get_short_url_view(api_client):
    """
    Test checking the correct return of a shortened link
    """
    short_link = ShortLinkFactory()
    response = api_client.get(reverse('get_short_link', kwargs={'code': short_link.code}))

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['url'] == short_link.url
    assert response_data['shortUrl'] == f"http://testserver/{short_link.code}"


@pytest.mark.django_db
def test_redirect_view(api_client, test_url):
    """
    Test checking the correct return of a shortened link
    """
    short_link = ShortLinkFactory(url=test_url)
    response = api_client.get(reverse('redirect_view', kwargs={'code': short_link.code}))

    assert response.status_code == 302
    assert response.url == short_link.url
