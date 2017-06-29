"""Assign web url routes to the names of different pages."""


def includeme(config):
    """Assign web url routes to the names of different pages."""
    config.add_static_view('static', 'pyramid_learning_journal:static')
    config.add_static_view('js', 'pyramid_learning_journal:static/js')
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('edit', '/journal/{id:\d+}/edit-entry')
