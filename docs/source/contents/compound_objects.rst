Compound Objects
================

About
-----

In University of Tennessee Digital Collections, digital objects that are made up of multiple works of various work types
that can all stand alone in the wild are considered to be :code:`Compound Objects`. :code:`Compound Objects` are not
historically considered to be paged and instead seen as related individuals. :code:`Compound Objects` are different from
:code:`Books` in these regards since :code:`Books` are paged and are made up of only :code:`Pages`. Since the works
that make up :code:`Compound Objects` can stand alone in the wild, they should not only be indexed but also found in OAI
and as members of IIIF collections.

Fedora Model
------------

Compound objects always have properites describing their work type and the collection(s) in which they belong. There
parts also have these properties plus a property for describing the compound object(s) of which they belong plus unique
properties that describe how they are ordered in a specific compound object.  For this reason, a Work could be a member
of multiple compound objects.

.. code-block:: turtle

    @prefix fedora: <info:fedora/fedora-system:def/relations-external#> .
    @prefix fedora-model: <info:fedora/fedora-system:def/model#> .
    @prefix islandora: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/rftaart:74> fedora-model:hasModel <info:fedora/islandora:compoundCModel> ;
        fedora:isMemberOfCollection <info:fedora/collections:rftaart>,
            <info:fedora/collections:rftacuratedart> .

    <info:fedora/rftaart:42> islandora:isSequenceNumberOfrftaart_74 "1" ;
        fedora-model:hasModel <info:fedora/islandora:sp_large_image_cmodel> ;
        fedora:isConstituentOf <info:fedora/rftaart:74> ;
        fedora:isMemberOfCollection <info:fedora/collections:rftaart> .

    <info:fedora/rftaart:51> islandora:isSequenceNumberOfrftaart_74 "2" ;
        fedora-model:hasModel <info:fedora/islandora:sp_videoCModel> ;
        fedora:isConstituentOf <info:fedora/rftaart:74> ;
        fedora:isMemberOfCollection <info:fedora/collections:rftaart> .

IIIF Manifest
-------------

Viewing Experience
------------------