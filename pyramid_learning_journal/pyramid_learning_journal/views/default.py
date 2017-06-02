"""Views for learning journal."""
from pyramid.view import view_config
from pyramid_learning_journal.data.data import posts
from pyramid.httpexceptions import HTTPNotFound


@view_config(route_name='home', renderer='../templates/main.jinja2')
def list_view(request):
    """Open home page with list of entries."""
    return {'page': 'home', "posts": posts}


@view_config(route_name='detail', renderer='../templates/entry.jinja2')
def detail_view(request):
    """Open individual entry page."""
    the_id = int(request.matchdict['id'])
    entry = None
    for item in posts:
        if item['id'] == the_id:
            entry = item
            break
    if entry is None:
        raise HTTPNotFound
    return {'page': 'detail', 'entry': entry}


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    """Open new entry page."""
    return {'page': 'create'}


@view_config(route_name='edit', renderer='../templates/edit_entry.jinja2')
def edit_view(request):
    """Open edit entry page."""
    the_id = int(request.matchdict['id'])
    entry = None
    for item in posts:
        if item['id'] == the_id:
            entry = item
            break
    if entry is None:
        raise HTTPNotFound
    return {'page': 'edit', 'entry': entry}
