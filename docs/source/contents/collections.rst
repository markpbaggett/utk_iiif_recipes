Collections
===========

About
-----

In University of Tennessee Digital Collections, collections are groups of related digital objects that are stored together.
Collections can belong to other collections and members of collections can belong to one or more collections.

Fedora Model
------------

A collection has very few structural properties. In our current repository, it should always have a :code:`fedora-model:hasModel`
stating its a Collection and a :code:`fedora:isMemberOfCollection` property stating its relationship to various collections.

.. code-block:: turtle

    @prefix ns0: <info:fedora/fedora-system:def/relations-external#> .
    @prefix ns1: <info:fedora/fedora-system:def/model#> .
    @prefix ns2: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/collections:rfta>
      ns0:isMemberOfCollection <info:fedora/digital:collections> ;
      ns1:hasModel <info:fedora/islandora:collectionCModel> .

A collection can be a member of multiple collections and has structural properties when this is a thing.

.. code-block:: turtle

    @prefix fedora: <info:fedora/fedora-system:def/relations-external#> .
    @prefix fedora-model: <info:fedora/fedora-system:def/model#> .

    <info:fedora/collections:kefauver> fedora-model:hasModel <info:fedora/islandora:collectionCModel> ;
        fedora:isMemberOfCollection <info:fedora/collections:mpa>, <info:fedora/digital:collections> .

IIIF Manifest
-------------

The IIIF manifest for a colleciton inherits the basic format for other manifests. For more information, see
:ref:`Base Manifest Properties`.

Collections should always have a :code:`type` property equal to :code:`Collection` and a :code:`viewingDirection` of
:code:`left-to-right`. The :code:`behavior` should be :code:`unordered`.

It is not assumed that a Collection has a curated thumbnail. For that reason, the :code:`thumbnail` property consists of
the thumbnails of all children objects.

The :code:`items` property includes each child with properties for :code:`id`, :code:`type`, :code:`label`, :code:`thumbnail`,
and :code:`homepage`.


Viewing Experience
------------------



Current Bugs and Things to Address
----------------------------------

1. The Collection object assumes all children are a :code:`Manifest` even though some may be a :code:`Collection`.
2. If the child is a :code:`Collection`, it is assumed there is a thumbnail and written to the :code:`thumbnail` property.