Audio
=====

About
-----

In University of Tennessee Digital Collections, digital objects whose primary file is sound are considered to be Audio.
Audio works usually consist of a preservation file stored in audio/mpge format with a PROXY_MP3 access copy.
Like other content models, a :code:`Audio` work may be a part of a :code:`Compound Object`.

Fedora Model
------------

Audio works always have structural properties that state their content model and the collections in which they are
members.  Their files may also have a :code:`bibframe:duration` that state how long they are.

.. code-block:: turtle

    @prefix fedora: <info:fedora/fedora-system:def/relations-external#> .
    @prefix fedora-model: <info:fedora/fedora-system:def/model#> .
    @prefix islandora: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/rfta:156> fedora-model:hasModel <info:fedora/islandora:sp-audioCModel> ;
        fedora:isMemberOfCollection <info:fedora/collections:rfta> .

    <info:fedora/rfta:156/PROXY_MP3> bibframe:duration "00:20:53" .

If they are parts of compound objects or have restrictions, they may also have additional properties.

IIIF Manifest
-------------

The IIIF manifest for an :code:`Audio` work inherits the basic format for other manifests. For more information, see
:ref:`Base Manifest Properties`.

This manifest is very similar to that of a video but with slightly few parts.

The :code:`items` property of the manifest for an Audio work has one canvas that points at the :code:`PROXY_MP3`
datastream. The :code:`Canvas` should have :code:`id`, :code:`type`, :code:`label`, :code:`thumbnail`, :code:`width`,
:code:`height`, :code:`duration`, :code:`items`, and :code:`annotations` properties following the IIIF Presentation v3
specification.


Viewing Experience
------------------
