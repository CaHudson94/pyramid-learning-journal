# pyramid-learning-journal

## Coverage:

pyramid_learning_journal/test_pyramid_learning_journal.py ..........

----------- coverage: platform linux, python 3.6.1-final-0 -----------
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
pyramid_learning_journal/data/__init__.py        0      0   100%
pyramid_learning_journal/data/data.py            1      0   100%
pyramid_learning_journal/views/__init__.py       0      0   100%
pyramid_learning_journal/views/default.py       27      0   100%
pyramid_learning_journal/views/notfound.py       4      0   100%
--------------------------------------------------------------------------
TOTAL                                           32      0   100%



## Author: Chris Hudson and Erik Enderlein

## Site:
 -https://quiet-springs-92243.herokuapp.com/

## Routes and Views:

### Routes:
-routes the home page to /
-routes the detail page for entries to /journal(entry id)
-routes the new entry page(create) to /journal/new-entry
-routes the edit page to /journal/(entry id)/edit-entry

### Views:
-list view for the home page(s) to main.html
-detail view for each entry page to entry.html
-create view for making a new entry to new-entry.html
-edit view for editing an entry to edit_entry.html
