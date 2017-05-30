from pyramid import testing
from pyramid.response import Response
import pytest

@pytest.fixture
def home_response():
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)

def test_home_view_returns_response_given_request(home_response):
    """Home view returns a Response object when given a request."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)


def test_home_view_is_good(home_response):
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.status_code == 200


def test_home_view_returns_proper_content(home_response):
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    expected_text = '<div class="menu-text"><h4><a href='
    assert expected_text in response.text
