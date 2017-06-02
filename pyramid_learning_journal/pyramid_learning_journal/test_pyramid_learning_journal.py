"""Test for views creation and link to html pages."""
from pyramid import testing
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound
from pyramid_learning_journal.data.data import posts
import pytest


@pytest.fixture
def testapp():
    """."""
    from pyramid_learning_journal import main


@pytest.fixture
def home_response():
    """Set fixture for home page."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def entry_response():
    """Set fixture for individual entry page."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    return response


@pytest.fixture
def edit_entry_response():
    """Set fixture for edit entry page."""
    from pyramid_learning_journal.views.default import edit_view
    request = testing.DummyRequest()
    response = edit_view(request)
    return response


@pytest.fixture
def new_entry_response():
    """Set fixture for new entry page."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_home_view_returns_response_given_request(home_response):
    """Home view returns a Response object when given a request."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)


def test_home_view_returns_proper_content(home_response):
    """Home view returns the actual content from the html."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    expected_text = '<title>A Journy into Code - Home</title>'
    assert expected_text in response.text


def test_new_entry_view_returns_response_given_request(new_entry_response):
    """New entry view returns a Response object when given a request."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert isinstance(response, Response)


def test_new_entry_view_returns_proper_content(new_entry_response):
    """New entry view returns the actual content from the html."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    expected_text = '<title>A Journy into Code - New Entry</title>'
    assert expected_text in response.text


def test_edit_entry_view_returns_response_given_request(edit_entry_response):
    """Edit entry view returns a Response object when given a request."""
    from pyramid_learning_journal.views.default import edit_view
    request = testing.DummyRequest()
    response = edit_view(request)
    assert isinstance(response, Response)


def test_edit_entry_view_returns_proper_content(edit_entry_response):
    """Edit entry view returns the actual content from the html."""
    from pyramid_learning_journal.views.default import edit_view
    request = testing.DummyRequest()
    response = edit_view(request)
    expected_text = '<title>A Journy into Code - Edit</title>'
    assert expected_text in response.text


def test_entry_view_returns_response_given_request(entry_response):
    """Entry view returns a Response object when given a request."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    assert isinstance(response, Response)


def test_entry_view_returns_proper_content(entry_response):
    """Entry view returns the actual content from the html."""
    from pyramid_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    expected_text = '<title>A Journy into Code - Entries</title>'
    assert expected_text in response.text