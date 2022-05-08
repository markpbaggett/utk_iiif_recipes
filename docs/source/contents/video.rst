Videos
======

About
-----

In University of Tennessee Digital Collections, digital objects that are moving images are considered to be Videos. Videos
usually consist of a preservation file stored in Matroska format with a MP4 access copy.  The MP4 may be curated and have
front matter and other content that is not present in the preservation copy. Its duration may also be different.  Like
other content models, a :code:`Video` may be a part of a :code:`Compound Object`.

Fedora Model
------------

Videos always have structural properties that state their content model the collections in which they are members.  Their
files mayb also have a :code:`bibframe:duration` that state how long they are.

.. code-block:: turtle

    @prefix fedora: <info:fedora/fedora-system:def/relations-external#> .
    @prefix fedora-model: <info:fedora/fedora-system:def/model#> .
    @prefix islandora: <http://islandora.ca/ontology/relsext#> .
    @prefix bibframe: <http://id.loc.gov/ontologies/bibframe/#> .

    <info:fedora/rfta:8> fedora-model:hasModel <info:fedora/islandora:sp_videoCModel> ;
        fedora:isMemberOfCollection <info:fedora/collections:rfta>, <info:fedora/collections:rftatest> .

    <info:fedora/rfta:8/MP4> bibframe:duration "00:57:15" .

If they are parts of compound objects or have restrictions, they may also have additional properties.


IIIF Manifest
-------------

The IIIF manifest for a :code:`Video` inherits the basic format for other manifests. For more information, see
:ref:`Base Manifest Properties`.

Viewing Experience
------------------

