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
    """Open new entry page."""
    with io.open(os.path.join(HERE, '../templates/new_entry.html')) as the_file:
        imported_page = the_file.read()
    return Response(imported_page)


def edit_view(request):
    """Open edit entry page."""
    with io.open(os.path.join(HERE, '../templates/edit_entry.html')) as the_file:
        imported_page = the_file.read()
    return Response(imported_page)
