Audio
=====

Generating a Sample Manifest for a World War II Oral History
------------------------------------------------------------

3.0.0 manifests for audio can be generated with for any audio like object using
`UTK Islandora 7 Manifest Generator <https://github.com/markpbaggett/utk_islandora7_manifest_generator>`_.

This can be run from any machine that has access to the Resource Index url.  No other credentials are required.

The application here is far from perfect and really serves mostly as a proof of concept.  There are bugs and gotchas
which I'll discuss below.

How Does It Work
----------------

To generate manifests, this content model requires three modules from the :code:`fedora` package and the :code:`Presentation3`
module from the :code:`iiif` package.

The :code:`fedora` package serves three purposes. The :code:`risearch` module is used to find the content model of the
object and the collection to which it belongs. This is done with the :code:`TuplesSearch` class. The :code:`mods` module
includes the :code:`MODSScraper` class which helps populate descriptive metadata elements for the manifest. By design,
this only works over http and does not use the API. It's also a bit of a mess.  It converts the MODS xml datastream to
an OrderedDict.  This isn't ideal.  It'd probably be better to interact with this via xpath. Because xpath isn't used,
the methods need to be considerate of typing. Also, with the exception of specific IIIF metadata elements that are
defined in the presentation specification, all other metadata elements are done at random as a proof of concept. In
order to be flexible to the needs to individual institutions, IIIF allows you to define your own descriptive metadata
elements, and the :code:`MODSScraper` class takes liberties to display certain elements but not all. See the descriptive
metadata section for recipes related to this. Finally, audio files need a duration element to be defined as a positive
floating point number in seconds. This is handled by the :code:`TechnicalMetadataScraper` class in the :code:`techhmd`
module. Because of its preciseness, the :code:`NLNZ Metadata Extractor` tool in :code:`FITS` is currently used as the
source data.

The :code:`Manifest3` class in the :code:`presentation3` module is used to build the actual manifest.  This module is
still a work in progress, but is currently able to build basic manfiests for audio content.

Generating a 3.0.0 Audio Manifest
---------------------------------

This application can be installed on any machine that has access to the RISearch interface. You can install this various
ways, but the easiest is most likely with `pipenv <https://github.com/pypa/pipenv>`_.

Once you've installed the application in a virtual environment with pipenv, you can generate a manifest by activating
the virtual environment and running the script like below.

.. code-block:: shell

    pipenv shell
    python run.py -p wwiioh:2001 -f manifest.json -r http://localhost:8080/fedora/risearch -s https://digital.lib.utk.edu

A Sample Audio Manifest
-----------------------

* `View in Mirador <https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/markpbaggett/utk_iiif_recipes/main/raw_manifests/wwiioh:2001.json>`_
* View in Universal Viewer

.. literalinclude:: ../../../raw_manifests/wwiioh:2001.json
    :language: json
    :linenos:
