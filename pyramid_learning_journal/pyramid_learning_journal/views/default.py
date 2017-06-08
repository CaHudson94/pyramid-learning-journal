"""Views for learning journal."""
from pyramid.view import view_config
from pyramid_learning_journal.models import Entry
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.security import remember, forget
from pyramid_learning_journal.security import check_credentials
import datetime

the_date = datetime.datetime.now()


@view_config(route_name='home', renderer='../templates/main.jinja2')
def list_view(request):
    """View for the home page with list of entries."""
    session = request.dbsession
    all_entries = session.query(Entry).order_by(Entry.id.desc()).all()
    return {
        'page': 'home',
        'posts': all_entries,
        'auth': request.authenticated_userid
    }


@view_config(route_name='detail', renderer='../templates/entry.jinja2')
def detail_view(request):
    """View to see an individual entry."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    if not entry:
        raise HTTPNotFound
    return {
        'page': 'detail',
        'entry': entry,
        'auth': request.authenticated_userid
    }


@view_config(
    route_name='create',
    renderer='../templates/new_entry.jinja2',
    permission='secret'
)
def create_view(request):
    """View for adding a new entry."""
    if request.method == "POST" and request.POST:
        if not request.POST['title'] or not request.POST['body']:
            return {
                'title': request.POST['title'],
                'body': request.POST['body'],
                'error': 'Please complete all fields'
            }

        new_entry = Entry(
            title=request.POST['title'],
            body=request.POST['body'],
            edit_date='Unedited',
            creation_date=the_date.strftime('%A, %-d %B, %Y, %-I:%M %P')
        )
        request.dbsession.add(new_entry)
        return HTTPFound(
            location=request.route_url('home')
        )
    return {'auth': request.authenticated_userid}


@view_config(
    route_name='edit',
    renderer='../templates/edit_entry.jinja2',
    permission='secret'
)
def edit_view(request):
    """View for editing an entry."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    new_date = the_date.strftime('%A, %-d %B, %Y, %-I:%M %P')
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return{
            'page': 'edit',
            'entry': entry,
            'auth': request.authenticated_userid
        }
    if request.method == "POST":
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        entry.edit_date = new_date
        request.dbsession.flush()
        return HTTPFound(
            location=request.route_url('detail', id=entry.id)
        )
    return {}


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    """Link to login button to authenticate user creds."""
    if request.method == "GET":
        return {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(
                location=request.route_url('home'),
                headers=headers
            )
        return {'error': 'That username or password does not compute!'}


@view_config(route_name='logout')
def logout(request):
    """Link to buttons to remove auth cookie."""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)
