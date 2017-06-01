"""Views for learning journal."""
from pyramid.view import view_config
from pyramid_learning_journal.data.data import posts
from pyramid.httpexceptions import HTTPNotFound


@view_config(route_name='home', renderer='../templates/list.jinja2')
def list_view(request):
    """Import page for main.html."""
    return {'page': 'home', 'posts': posts}


@view_config(route_name='detail', renderer='../templates/entry.jinja2')
def detail_view(request):
    """Import page for entry.html."""
    the_id = int(request.matchdict['id'])
    try:
        post = posts[the_id]
    except IndexError:
        raise HTTPNotFound
    return {'page': 'detail', 'title': post['title'],
            'date': post['creation_date'], 'body': post['body']}


@view_config(route_name='create', renderer='../templates/new_entry.jinja2')
def create_view(request):
    """Import page for new_entry.html."""
    return {'page': 'create'}


@view_config(route_name='edit', renderer='../templates/edit_entry.jinja2')
def edit_view(request):
    """Import page for edit_entry.html."""
    the_id = int(request.matchdict['id'])
    try:
        post = posts[the_id]
    except IndexError:
        raise HTTPNotFound
    return {'page': 'edit', 'title': post['title'],
            'date': post['creation_date'], 'body': post['body']}
