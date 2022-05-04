Base Manifest
=============

.. _Base Manifest Properties:

About
-----

This document describes rules that tend to be inherited by all content models unless otherwise specified in the model's
corresponding doc or in the specific property definition below.

Root Properties
---------------

`IIIF Assemble <https://github.com/utkdigitalinitiatives/iiif_assemble>`_ generates these properties at the root level
of the manifest.  Practices follow the `IIIF Presentation v3 Specification <https://iiif.io/api/presentation/3.0/>`_ and
the `Cookbook of IIIF Recipes <https://iiif.io/api/cookbook/>`_.

========
@context
========

The context property is always the first property in the manifest. For UTK collections, it is always an array with
:code:`https://iiif.io/api/presentation/3/context.json` as the last value (unless it is the only value).  Any other
extensions we use appear before this value. As of May 1, 2022, no other extensions are used.

See `4.6 Linked Data Context and Extensions <https://iiif.io/api/presentation/3.0/#46-linked-data-context-and-extensions>`_.

==
id
==

The :code:`id` property is a technical property that identifies the resource.  At the manifest level, this is always the
:code:`https` uri to the Manifest. (e.g. :code:`https://digital.lib.utk.edu/assemble/manifest/acwiley/280`)

IIIF Assemble translates this value and creates a dereferenceable IIIF manifest at this URI based on two patterns. For
collection objects, the pattern is :code:`https://digital.lib.utk.edu/assemble/collection/` plus the persistent identifier
(PID) of the object with the :code:`:` replaced with a :code:`/`.
(e.g. :code:`https://digital.lib.utk.edu/assemble/collection/collections/rfta`)

See `3.2. Technical Properties: id <https://iiif.io/api/presentation/3.0/#id>`_ for more information.

====
type
====

The :code:`type` property describes the type of class of the resource. The value is always a string. If the object is
not a collection, this value is always :code:`Manifest` at root.  Otherwise, it is :code:`Collection`.

See `3.2. Technical Properties: type <https://iiif.io/api/presentation/3.0/#type>`_ for more information.

=====
label
=====

The :code:`label` property is descriptive and is required at root on the manifest. Follow the presentation v3 specification,
the value MUST be a JSON object.

For UTK collections, this value is always the following where :code:`TITLE OF OBJECT` is equal to the value(s) of the
xpath expression :code:`titleInfo[not(@type="alternative")][not(@lang)]` expressed against the MODS record of the
related digital object:

.. code-block:: json

    {
        "en":
            ["TITLE OF OBJECT"]
    }

See `3.1. Descriptive Properties: label <https://iiif.io/api/presentation/3.0/#label>`_ for more information.

=======
summary
=======

The :code:`summary` property is a short textual summary intended to be conveyed to the user when the :code:`metadata`
entries for the resource are not being displayed. This could be used as a brief description for item level search
results, for small-screen environments, or as an alternative user interface when the :code:`metadata` property is not
currently being rendered.

The :code:`summary` property follows the same patten as label. If the expression :code:`abstract[not(@lang)]` against a
digital object's MODS record has a value, a summary is added to the manifest like this:

.. code-block:: json

    {
        "en":
            ["SUMMARY"]
    }

See `3.1. Descriptive Properties: summary <https://iiif.io/api/presentation/3.0/#summary>`_ for more information.

======
rights
======

The :code:`rights` property is a string that identifies a license or rights statement that applies to the content of the
digital object. It is modelled as a string.

The value of :code:`rights` is present if the XPATH expression :code:`accessCondition[@xlink:href]` against the object's
MODS record has a value.

See `3.1. Descriptive Properties: rights <https://iiif.io/api/presentation/3.0/#rights>`_ for more information.

========
metadata
========

The :code:`metadata` property is an ordered list of descriptions to be displayed to the user when they interact with the
resource, given as pairs of human readable label and value entries. The content of these entries is intended for
presentation only; descriptive semantics should not be inferred. An entry might be used to convey information about the
creation of the object, a physical description, ownership information, or other purposes.

The value of the :code:`metadata` property must be an array of JSON objects, where each item in the array has both
:code:`label` and :code:`value` properties. The values of both :code:`label` and :code:`value` must be JSON objects, as
described in the `languages section <https://iiif.io/api/presentation/3.0/#language-of-property-values>`_ of the IIIF
Presentation v3 specification.

Because UTK metadata is always intended to be displayed to English speakers, we always use the :code:`en` property.

Our current metadata values are:

+------------------------+-------------------------------------------------------------------------+
| Label                  | Expression                                                              |
+========================+=========================================================================+
| Alternative Title      | titleInfo[@type="alternative"]                                          |
+------------------------+-------------------------------------------------------------------------+
| Table of Contents      | tableOfContents                                                         |
+------------------------+-------------------------------------------------------------------------+
| Publisher              | originInfo/publisher                                                    |
+------------------------+-------------------------------------------------------------------------+
| Date                   | originInfo/dateCreated|originInfo/dateOther                             |
+------------------------+-------------------------------------------------------------------------+
| Publication Date       | originInfo/dateIssued                                                   |
+------------------------+-------------------------------------------------------------------------+
| Format                 | physicalDescription/form[not(@type="material")]                         |
+------------------------+-------------------------------------------------------------------------+
| Extent                 | physicalDescription/extent                                              |
+------------------------+-------------------------------------------------------------------------+
| Subject                | subject[not(@displayLabel="Narrator Class")]/topic                      |
+------------------------+-------------------------------------------------------------------------+
| Narrator Role          | subject[@displayLabel="Narrator Class"]/topic                           |
+------------------------+-------------------------------------------------------------------------+
| Place                  | subject/geographic                                                      |
+------------------------+-------------------------------------------------------------------------+
| Time Period            | subject/temporal                                                        |
+------------------------+-------------------------------------------------------------------------+
| Description            | abstract[not(@lang)]                                                    |
+------------------------+-------------------------------------------------------------------------+
| Descripción            | abstract[@lang="spa"]                                                   |
+------------------------+-------------------------------------------------------------------------+
| Titulo                 | titleInfo[@lang="spa"]/title                                            |
+------------------------+-------------------------------------------------------------------------+
| Publication Identifier | identifier[@type="isbn"]||identifier[@type="issn"]                      |
+------------------------+-------------------------------------------------------------------------+
| Browse                 | note[@displayLabel="Browse"]                                            |
+------------------------+-------------------------------------------------------------------------+
| Language               | language/languageTerm                                                   |
+------------------------+-------------------------------------------------------------------------+
| *Role Term*            | mods:name[mods:role[mods:roleTerm[text()='{$ROLETERM}']]]/mods:namePart |
+------------------------+-------------------------------------------------------------------------+

See `3.1. Descriptive Properties: metadata <https://iiif.io/api/presentation/3.0/#metadata>`_ for more information.

=================
requiredStatement
=================

The :code:`requiredStatement` property includes text that MUST be displayed when a resource is displayed or used. It
MUST be a JSON-like object with corresponding labels and values that should be displayed.

For digital objects from our repository, this property exists if the XPATH expression :code:`recordInfo/recordContentSource`
returns a value when executed against the MODS record.  When it does, the :code:`requiredStatement` property gets a
value like this:

.. code-block:: json

    {
      "requiredStatement": {
        "label": { "en": [ "Provided by" ] },
        "value": { "en": [ "VALUE OF XPATH EXPRESSION" ] }
      }
    }

See `3.1. Descriptive Properties: requiredStatement <https://iiif.io/api/presentation/3.0/#requiredStatement>`_ for more
information.

========
provider
========

The :code:`provider` property represents a n organization or person that contributed to providing the content of the
resource. Clients can then display this information to the user to acknowledge the provider’s contributions. This
differs from the :code:`requiredStatement` property, in that the data is structured, allowing the client to do more than
just present text but instead have richer information about the people and organizations to use in different interfaces.

Despite this, we use the property to always describe ourselves:

.. code-block:: json

    {
      "provider": [
        {
          "id": "https://www.lib.utk.edu/about/",
          "type": "Agent",
          "label": { "en": [ "University of Tennessee, Knoxville. Libraries" ] },
          "homepage": [
            {
              "id": "https://www.lib.utk.edu/",
              "type": "Text",
              "label": { "en": [ "University of Tennessee Libraries Homepage" ] },
              "format": "text/html"
            }
          ],
          "logo": [
            {
              "id": "https://utkdigitalinitiatives.github.io/iiif-level-0/ut_libraries_centered/full/full/0/default.jpg",
              "type": "Image",
              "format": "image/png",
              "height": 200,
              "width": 200
            }
          ],
        }
      ]
    }

See `3.1. Descriptive Properties: provider <https://iiif.io/api/presentation/3.0/#provider>`_ for more
information.

=========
thumbnail
=========

Each manifest should have a :code:`thumbnail` property.  This property is a  content resource, such as a small image or
short audio clip, that represents the resource that has the thumbnail property. A resource may have multiple thumbnail
resources that have the same or different type and format.

As a general rule, the manifest of a work is always represented by it's thumbnail datastream. The properties should be
populated by the results of Cantaloupe Image API requests. It should look something like this:

.. code-block:: json

    {
        "thumbnail": [
            "id": "https://digital.lib.utk.edu/iiif/2/collections~islandora~object~rftaart%3A74~datastream~TN/full/max/0/default.jpg",
            "width": 200,
            "height": 157,
            "service": [
                {
                    "@id": "https://digital.lib.utk.edu/iiif/2/collections~islandora~object~rftaart%3A74~datastream~TN",
                    "@type": "http://iiif.io/api/image/2/context.json",
                    "@profile": "http://iiif.io/api/image/2/level2.json"
                }
            ],
            "type": "Image",
            "format" "image/jpeg"
        ]
    }

Audio and video works may also have a :code:`duration` property.

Since collections do not necessarily have a representative thumbnail in the repository, the value of its :code:`thumbnail`
property is derived from the thumbnails of all objects in the collection.

See `3.1. Descriptive Properties: thumbnail <https://iiif.io/api/presentation/3.0/#thumbnail>`_ for more information.

=====
items
=====

The :code:`items` property includes the list of child resources of the manifest.  Most of the time, at root, :code:`items`
contains all the Works canvases. The exception is on Collection manifests where this contains a list of all the collections
manifests.

A specific method is used to build this list for Books and Compound Objects since they are multi-canvased.  All other
work types use another method.

For specific information regarding this property, see the associated work type.

See `3.4 Structural Properties: items <https://iiif.io/api/presentation/3.0/#items>`_ for more information.

=======
seeAlso
=======

The :code:`seeAlso` property is a machine-readable resource such as an XML or RDF description that is related to the
current resource.

For UT Collections, this always refers to the MODS record and looks like this:

.. code-block:: json

    "seeAlso": [
        {
          "id": "https:\/\/digital.lib.utk.edu\/collections\/islandora\/object\/rfta%3A8\/datastream\/MODS",
          "type": "Dataset",
          "label": {
            "en": [
              "Bibliographic Description in MODS"
            ]
          },
          "format": "application\/xml",
          "profile": "http:\/\/www.loc.gov\/standards\/mods\/v3\/mods-3-5.xsd"
        }
      ]
    }

See `3.3.1. External Links: partOf <https://iiif.io/api/presentation/3.0/#partOf>`_ for more information.

======
partOf
======

The :code:`partOf` property lists the IIIF resources that contain this one.  It may be a collection manifest or the
manifest of a compound object. The :code:`type` property should describe what the containing manifest is. If the object
is in multiple collections or multiple compound objects, all will be included.

.. code-block:: json

    {
      "partOf": [
        {
          "id": "https:\/\/digital.lib.utk.edu\/assemble\/collection\/collections\/rfta",
          "type": "Collection"
        },
        {
          "id": "https:\/\/digital.lib.utk.edu\/assemble\/collection\/collections\/rftatest",
          "type": "Collection"
        }
      ]
    }

See `3.3.1. Linking Properties: partOf <https://iiif.io/api/presentation/3.0/#partOf>`_ for more information.

========
homepage
========

The :code:`homepage` property is a web page that is about the object represented by the resource.  Usually, this is the
landing page in Islandora.  If the object's main page is not its Islandora page, this value should refer to that.

.. code-block:: json

    {
      "homepage": [
        {
          "id": "https:\/\/rfta.lib.utk.edu\/interviews\/object\/seemona-and-daniel-whaley-2019-09-20",
          "label": {
            "en": [
              "Interview with Seemona and Daniel Whaley, 2019-09-20"
            ]
          },
          "type": "Text",
          "format": "text\/html"
        }
      ],
    }

See `3.3.1. Linking Properties: homepage <https://iiif.io/api/presentation/3.0/#homepage>`_ for more information.

========
behavior
========

The :code:`behavior` property dictates the set of user experience features that we would prefer clients to use when
presenting the resource. This property must be an array of strings that align with presentation v3 or an extension.

Most work types do not use this, but some do including :code:`CompoundObjects`, :code:`Books`, and :code:`Collections`.

For more information about unique uses, see details in the work type definitions.

See `3.2 Technical Properties: behavior <https://iiif.io/api/presentation/3.0/#behavior>`_ for more information.

================
viewingDirection
================

The :code:`viewingDirection` property dictates the direction in which a set of Canvases should be displayed to the user.

Most work types do not use this unless there are specific expectations for viewing direction.

For more information about unique uses, see details in the work type definitions.

See `3.2 Technical Properties: viewingDirection <https://iiif.io/api/presentation/3.0/#viewingdirection>`_ for more information.

==================
accompanyingCanvas
==================

The :code:`accompanyingCanvas` property is a single Canvas that provides additional content for use while rendering the
resource. Examples include an image to show while a duration-only Canvas is playing audio; or background audio to play
while a user is navigating an image-only Manifest.

Only audio files have this currently. For more information about this, see details in the work type definition.

See `3.1 Descriptive Properties: accompanyingCanvas <https://iiif.io/api/presentation/3.0/#accompanyingCanvas>`_ for more
information.