"""Views for learning journal."""
from pyramid.view import view_config
from pyramid_learning_journal.models import Entry
from pyramid.httpexceptions import HTTPNotFound
import datetime

the_date = datetime.datetime.now()


@view_config(route_name='home', renderer='../templates/main.jinja2')
def list_view(request):
    """View for the home page with list of entries."""
    session = request.dbsession
    all_entries = session.query(Entry).order_by(Entry.id.desc()).all()
    return {'page': 'home', "posts": all_entries}


@view_config(route_name='detail', renderer='../templates/entry.jinja2')
def detail_view(request):
    """View to see an individual entry."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    if not Entry:
        raise HTTPNotFound
    return {'page': 'detail', 'entry': entry}


@view_config(route_name='create', renderer='../templates/new_entry.jinja2')
def create_view(request):
    """View for adding a new entry."""
    return {'page': 'create'}


@view_config(route_name='edit', renderer='../templates/edit_entry.jinja2')
def edit_view(request):
    """View for editing an entry."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).all(the_id)
    new_date = the_date.strftime('%A, %-d %B, %Y, %-I:%M %P')
    if not Entry:
        raise HTTPNotFound
    return {'page': 'edit', 'entry': entry, 'edit_date': new_date}
