================
Docstirngviewer
================

Docstringviewer is a Django app which displays docstrings of all python modules and objects
inside them for project. 

Detailed documentation is in the "docs" directory.


Installation
------------
1. You can istall it directly by ``pip``::

    pip install git+git://github.com/josipgrgurica/django-docstringviewer.git

2. Vou can add this line to you requriments.txt::

   -e git://github.com/jgrgurica/django-docstringviewer.git#egg=django-docstringviewer


Quick start
-----------

1. Add "docstringviewer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'docstringviewer',
    ]

2. Include the docstingviewerURLconf in your project urls.py like this::

    url(r'^docstringviewer/', include('docstringviewer.urls')),

3. Assign your project root to ``ROOT_DOCS_DIR`` in your settings file::
   
    import os

    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    ROOT_DOCS_DIR = PROJECT_ROOT

