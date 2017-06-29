"""Views for learning journal."""
from pyramid.response import Response
from pyramid.view import view_config
import os
import io

HERE = os.path.dirname(__file__)

the_date = datetime.datetime.now()

def list_view(request):
    """Open home page with list of entries."""
    with io.open(os.path.join(HERE, '../templates/main.html')) as the_file:
        imported_page = the_file.read()
    return Response(imported_page)


def detail_view(request):
    """Open individual entry page."""
    with io.open(os.path.join(HERE, '../templates/entry.html')) as the_file:
        imported_page = the_file.read()
    return Response(imported_page)


def create_view(request):
    """View for adding a new entry."""
    return {'page': 'create'}


def edit_view(request):
    """View for editing an entry."""
    the_id = int(request.matchdict['id'])
    entry = None
    for item in posts:
        if item['id'] == the_id:
            entry = item
            break
    if entry is None:
        raise HTTPNotFound
    return {'page': 'edit', 'entry': entry}