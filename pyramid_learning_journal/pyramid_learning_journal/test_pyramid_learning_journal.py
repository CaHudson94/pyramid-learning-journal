"""Test for views creation and link to html pages."""
from pyramid import testing
from pyramid.response import Response
import pytest
from pyramid_learning_journal.views.default import (
    list_view,
    create_view,
    edit_view,
    detail_view
)


@pytest.fixture
def home_response():
    """Set fixture for home page."""
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def entry_response():
    """Set fixture for individual entry page."""
    request = testing.DummyRequest()
    response = detail_view(request)
    return response


@pytest.fixture
def edit_entry_response():
    """Set fixture for edit entry page."""
    request = testing.DummyRequest()
    response = edit_view(request)
    return response


@pytest.fixture
def new_entry_response():
    """Set fixture for new entry page."""
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_home_view_returns_response_given_request(home_response):
    """Home view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)


def test_home_view_is_good(home_response):
    """Home view hass a 200 ok."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.status_code == 200


def test_home_view_returns_proper_content(home_response):
    """Home view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = list_view(request)
    expected_text = '<div class="entries">'
    assert expected_text in response.text


def test_new_entry_view_returns_response_given_request(new_entry_response):
    """New entry view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = create_view(request)
    assert isinstance(response, Response)


def test_new_entry_view_is_good(new_entry_response):
    """New entry view hass a 200 ok."""
    request = testing.DummyRequest()
    response = create_view(request)
    assert response.status_code == 200


def test_new_entry_view_returns_proper_content(new_entry_response):
    """New entry view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = create_view(request)
    expected_text = '<h2>New Entry</h2>'
    assert expected_text in response.text


def test_edit_entry_view_returns_response_given_request(edit_entry_response):
    """Edit entry view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = edit_view(request)
    assert isinstance(response, Response)


def test_edit_entry_view_is_good(edit_entry_response):
    """Edit entry view hass a 200 ok."""
    request = testing.DummyRequest()
    response = edit_view(request)
    assert response.status_code == 200


def test_edit_entry_view_returns_proper_content(edit_entry_response):
    """Edit entry view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = edit_view(request)
    expected_text = '<h2>Edit Entry</h2>'
    assert expected_text in response.text


def test_entry_view_returns_response_given_request(entry_response):
    """Entry view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = detail_view(request)
    assert isinstance(response, Response)


def test_entry_view_is_good(entry_response):
    """Entry view hass a 200 ok."""
    request = testing.DummyRequest()
    response = detail_view(request)
    assert response.status_code == 200


def test_entry_view_returns_proper_content(entry_response):
    """Entry view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = detail_view(request)
    expected_text = '<h3>Example entry</h3>'
    assert expected_text in response.text
