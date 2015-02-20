================
Docstirngviewer
================

Docstringviewer is a Django app which displays docstrings or all python modules and objects
inside them for project. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "docstringviewer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'docstringviewer',
    ]


2. Include the polls URLconf in your project urls.py like this::

    url(r'^docstringviewer/', include('docstringviewer.urls')),


