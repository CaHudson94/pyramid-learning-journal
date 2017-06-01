"""Views for learning journal."""
from pyramid.response import Response
import os
import io

HERE = os.path.dirname(__file__)


def list_view(request):
    """Import page for main.html."""
    with io.open(os.path.join(HERE, '../templates/main.html')) as the_file:
        imported_page = the_file.read()

    return Response(imported_page)


def detail_view(request):
    """Import page for entry.html."""
    with io.open(os.path.join(HERE, '../templates/entry.html')) as the_file:
        imported_page = the_file.read()

    return Response(imported_page)


def create_view(request):
    """Import page for new_entry.html."""
    with io.open(os.path.join(HERE, '../templates/new_entry.html')) as the_file:
        imported_page = the_file.read()

    return Response(imported_page)


def edit_view(request):
    """Import page for edit_entry.html."""
    with io.open(os.path.join(HERE, '../templates/edit_entry.html')) as the_file:
        imported_page = the_file.read()

    return Response(imported_page)
