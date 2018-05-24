"""Setup for Pyramid Learning Journal."""
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'ipython',
    'pyramid_ipython',
    'psycopg2',
    'passlib',
    'webtest',
]

tests_require = [
    'WebTest >= 1.3.1',
    'pytest',
    'pytest-cov',
    'tox',
    'faker',
]

setup(
    name='pyramid_learning_journal',
    version='0.0',
    description='Learning Journal',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Chris Hudson',
    author_email='c.ahudson84@yahoo.com',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pyramid_learning_journal:main',
        ],
        'console_scripts': [
            'initializedb = pyramid_learning_journal.scripts.initializedb:main',
        ]
    },
)
