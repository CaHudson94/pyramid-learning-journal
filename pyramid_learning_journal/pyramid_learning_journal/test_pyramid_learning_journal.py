"""Test for views creation and link to html pages."""
from pyramid import testing
from pyramid_learning_journal.data.data import posts
import pytest


@pytest.fixture
def testapp():
    """Create a test application to use for functional tests."""
    from pyramid_learning_journal import main
    from webtest import TestApp
    app = main({})
    return TestApp(app)


@pytest.fixture
def home_response():
    """Set fixture for home page."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def new_entry_response():
    """Set fixture for new entry page."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_home_view_page_is_home(home_response):
    """Test list view is routed to home page."""
    from pyramid_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert response['page'] is 'home'


def test_home_route_has_list_of_entries(testapp):
    """Test if there are the right amount of entries on the home page."""
    response = testapp.get('/')
    html = response.html
    assert html.find()
    num_list_items = (len(html.find_all('h3')))
    assert num_list_items == len(posts)


def test_home_view_returns_proper_content(testapp):
    """Home view returns the actual content from the html."""
    response = testapp.get('/')
    html = response.html
    expected_text = '<ol class="pagination">'
    assert expected_text in str(html)


def test_new_entry_view_page_is_create(new_entry_response):
    """Test create view is routed to new entry page."""
    from pyramid_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert response['page'] is 'create'


def test_new_entry_view_returns_proper_content(testapp):
    """New entry view returns the actual content from the html."""
    response = testapp.get('/journal/new-entry')
    html = response.html
    expected_text = '<div class="large-6 columns"><h2>New Entry</h2></div>'
    assert expected_text in str(html)


def test_edit_entry_view_returns_proper_content(testapp):
    """Edit entry view returns the actual content from the html."""
    response = testapp.get('/journal/1/edit-entry')
    html = response.html
    assert html.find()
    expected_text = '<div class="large-6 columns grade1"></div>'
    assert expected_text in str(html)


def test_detail_entry_has_single_entry(testapp):
    """Test that the detail page only brings up one entry."""
    response = testapp.get('/journal/1')
    html = response.html
    assert html.find()
    num_list_items = (len(html.find_all('h3')))
    assert num_list_items == 1


def test_detail_entry_returns_proper_content(testapp):
    """Entry view returns a Response object when given a request."""
    response = testapp.get('/journal/1')
    html = response.html
    assert html.find()
    expected_text = '<div class="entries">'
    assert expected_text in str(html)


def test_detail_view_with_bad_id(testapp):
    """."""
    response = testapp.get('/journal/9001', status=404)
    assert "These are not the pages you're looking for!" in response.text


def test_edit_view_with_bad_id(testapp):
    """."""
    response = testapp.get('/journal/9001/edit-entry', status=404)
    assert "These are not the pages you're looking for!" in response.text
