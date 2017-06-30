# pyramid-learning-journal

## Coverage:

Step1:

pyramid_learning_journal/test_pyramid_learning_journal.py ............

----------- coverage: platform linux, python 3.6.1-final-0 -----------
Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
pyramid_learning_journal/views/default.py      21      0   100%


========================== 12 passed in 2.73 seconds ===========================
___________________________________ summary ____________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)

Step2:

pyramid_learning_journal/test_pyramid_learning_journal.py ........

----------- coverage: platform linux, python 3.6.1-final-0 -----------
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
pyramid_learning_journal/data/__init__.py        0      0   100%
pyramid_learning_journal/data/data.py            1      0   100%
pyramid_learning_journal/views/__init__.py       0      0   100%
pyramid_learning_journal/views/default.py       17      0   100%
pyramid_learning_journal/views/notfound.py       4      0   100%
--------------------------------------------------------------------------
TOTAL                                           22      0   100%


=========================== 8 passed in 1.53 seconds ===========================
___________________________________ summary ____________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)

Step 3:

----------- coverage: platform linux, python 3.6.1-final-0 -----------
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
pyramid_learning_journal/data/__init__.py        0      0   100%
pyramid_learning_journal/data/data.py            1      0   100%
pyramid_learning_journal/routes.py               7      0   100%
pyramid_learning_journal/views/__init__.py       0      0   100%
pyramid_learning_journal/views/default.py       28      0   100%
pyramid_learning_journal/views/notfound.py       4      0   100%
--------------------------------------------------------------------------
TOTAL                                           40      0   100%


========================== 25 passed in 1.87 seconds ===========================
___________________________________ summary ____________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)

Step 4:

----------- coverage: platform linux, python 3.6.1-final-0 -----------
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
pyramid_learning_journal/data/__init__.py        0      0   100%
pyramid_learning_journal/data/data.py            1      0   100%
pyramid_learning_journal/routes.py               7      0   100%
pyramid_learning_journal/views/__init__.py       0      0   100%
pyramid_learning_journal/views/default.py       39      0   100%
pyramid_learning_journal/views/notfound.py       4      0   100%
--------------------------------------------------------------------------
TOTAL                                           51      0   100%


========================== 29 passed in 1.93 seconds ===========================
___________________________________ summary ____________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)



## Author: Chris Hudson and Erik Enderlein

## Site:
 -http://chris-hudson-journal.herokuapp.com/

## Routes and Views:

### Routes:
-routes the home page to /
-routes the detail page for entries to /journal(entry id)
-routes the new entry page(create) to /journal/new-entry
-routes the edit page to /journal/(entry id)/edit-entry

### Views:
-list view for the home page(s) to main.jinja2
-detail view for each entry page to entry.jinja2
-create view for making a new entry to new-entry.jinja2
-edit view for editing an entry to edit_entry.jinja2

