Books
=====

Generating A Sample 2.1.1 Book Manifest
---------------------------------------

2.1.1 manifests can be generated for any book like object using `UTK Book to Presentation Manifest <https://github.com/markpbaggett/utk_book_presentation_manifest>`_.
This can be run from any machine that has access to the Resource Index url.  No other credentials are required.

The application here is far from perfect and really serves mostly as a proof of concept.  There are bugs and gotchas
which I'll discuss below.

How Does It Work
^^^^^^^^^^^^^^^^

Currently, this application consists of two packages: :code:`fedora` and :code:`iiif`. The :code:`fedora` package serves
two purposes:  finding relationships to other Fedora objects and scraping descriptive metadata.

Finding relationships is done via the :code:`risearch` module. There are multiple classes here, but the one of primary
interest in :code:`TuplesSearch`. :code:`TuplesSearch` allows us to find out what collection a book belongs to and get
an ordered list of page objects that relate to that book.

Scraping descriptive metadata is done with the :code:`ModsScraper` class in the :code:`mods` module. By design, this only
works over http and does not use the API. It's also a bit of a mess.  It converts the MODS xml datastream to an
OrderedDict.  This isn't ideal.  It'd probably be better to interact with this via xpath. Because xpath isn't used, the
methods need to be considerate of typing.  This is done in certain cases (i.e. :code:`get_navigation_date()`), but not
always.  Because of this, there are probably records in our repository that would throw an exception. Also, descriptive
metadata that is scraped is done so at random and is definitely not exhaustive. Any contributions here would be welcomed.

The :code:`iiif` package includes the :code:`manifest` module.  The classes here are used to build the presentation
manifest and its various canvases.

Generating a Book Manifest
^^^^^^^^^^^^^^^^^^^^^^^^^^

This application can be installed on any machine that has access to the RISearch interface. You can install this various
ways, but the easiest is most likely with `pipenv <https://github.com/pypa/pipenv>`_.

Once you've installed the application in a virtual environment with pipenv, you can generate a manifest by activating
the virtual environment and running the script like below.

.. code-block:: shell

    pipenv shell
    python run.py -b agrtfhs:2275 -f manifest.json -r http://localhost:8080/fedora/risearch -s https://digital.lib.utk.edu


A Sample Book Manifest
^^^^^^^^^^^^^^^^^^^^^^

* `View in Universal Viewer <http://universalviewer.io/uv.html?manifest=https://raw.githubusercontent.com/markpbaggett/utk_iiif_recipes/main/raw_manifests/sample_book.json>`_
* `View in Mirador <https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/markpbaggett/utk_iiif_recipes/main/raw_manifests/sample_book.json>`_

.. literalinclude:: ../../../raw_manifests/sample_book.json
    :language: json
    :linenos:
