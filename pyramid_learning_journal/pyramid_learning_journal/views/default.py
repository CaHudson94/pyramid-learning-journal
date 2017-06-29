"""Views for learning journal."""
from pyramid.response import Response
from pyramid.view import view_config
import os
import io

HERE = os.path.dirname(__file__)

the_date = datetime.datetime.now()

def list_view(request):
    """View for the home page with list of entries."""
    session = request.dbsession
    all_entries = session.query(Entry).order_by(Entry.id.desc()).all()
    return {'page': 'home', "posts": all_entries}


def detail_view(request):
    """View to see an individual entry."""
    the_id = int(request.matchdict['id'])
    print(the_id)
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    if not entry:
        raise HTTPNotFound
    return {'page': 'detail', 'entry': entry}


def create_view(request):
    """View for adding a new entry."""
    return {'page': 'create'}


def edit_view(request):
    """View for editing an entry."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    new_date = the_date.strftime('%A, %-d %B, %Y, %-I:%M %P')
    if not entry:
        raise HTTPNotFound
    return {'page': 'edit', 'entry': entry}