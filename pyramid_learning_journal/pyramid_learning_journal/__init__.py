"""Returns a Pyramid WSGI application."""
from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application."""
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_learning_journal.routes')
    config.include('pyramid_learning_journal.models')
    config.add_static_view(name='static', path='pyramid_learning_journal:static')
    config.scan()
    return config.make_wsgi_app()
