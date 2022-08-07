.. _The navPlace Property:

The navPlace Property
=====================

About
-----

Many UTK works that manifests describe include cartographic and coordinate information. This document details how we will
implement :code:`navPlace` for our works so that IIIF viewers that support the property can display our works on a map.

@context
--------

The :code:`navPlace` property exists in a `separate IIIF extension <http://iiif.io/api/extension/navplace/context.json>`_.
In order to use :code:`navPlace`, we must include this extension, `<http://iiif.io/api/extension/navplace/context.json>`_,
in the :code:`@context` property before the `<http://iiif.io/api/presentation/3/context.json>`_ value.

.. code-block:: json

    {
        "@context":[
            "http://iiif.io/api/extension/navplace/context.json",
            "http://iiif.io/api/presentation/3/context.json"
        ]
    }

navPlace on a Manifest
----------------------

Technically, the :code:`navPlace` property is valid on a :code:`Collection`, :code:`Manifest`, :code:`Range`,
or :code:`Canvas`.  Our first implementation of :code:`navPlace` will be on the :code:`Manifest`.

Unlike other properties, :code:`navPlace` follows a specific pattern.  The value of the property must be a JSON object
that follows the requirements for a GeoJSON Feature Collection as described in `Section 2.2.2 <https://iiif.io/api/extension/navplace/#222-feature-collection>`_.
The value should be an embedded Feature Collection. However, the value may be a referenced Feature Collection.
Feature Collections referenced in the :code:`navPlace` property must have the :code:`id` and :code:`type` properties.
Referenced Feature Collections must not have the :code:`features` property, such that clients are able to recognize that
it should be retrieved in order to be processed.

For our manifests, if a work has a value in the :code:`mods:subject/mods:cartographics/mods:coordinates` xpath of its MODS
record it will get a :code:`navPlace` property on the :code:`Manifest`.

For our manifests, the :code:`navPlace` property will always have three properties: :code:`id`, :code:`type`, :code:`features`.
The :code:`type` property will always be :code:`FeatureCollection`. The :code:`id` property will be unique for the
:code:`FeatureCollection` and will be equal to the base manifest :code:`id` concatenated with the value :code:`/feature-collection/1`.

.. code-block:: json

    {
        "navPlace":
            "id": "https://digital.lib.utk.edu/assemble/manifest/rfta/8/feature-collection/1",
            "type": "FeatureCollection",
            "features": []
    }

The :code:`features` property will be an array. In the array will be a :code:`Feature` for each matching value of
:code:`mods:subject/mods:cartographics/mods:coordinates`.  Each :code:`Feature` will have these properties: :code:`id`,
:code:`type`, :code:`properties`, and :code:`geometry`. The :code:`type` property will always be :code:`Feature`.  To
ensure uniqueness, each :code:`Feature` :code:`id` will be equal to the :code:`id` of the :code:`id` of the Manifest
concatenated with :code:`/feature/1`. It's important to recognize that currently there is no plan to add :code:`FeatureCollection`
:code:`id` to uri.  Because of that, we could have id issues if we were to add :code:`navPlace` to :code:`Canvas` or
:code:`Range`. The :code:`properties` property is described `here <https://iiif.io/api/extension/navplace/#32-context-considerations-for-geojson-ld-properties>`_.
For our implementation, it will have :code:`manifest` and :code:`label` properties. The :code:`manifest`
property is equivalent to the value of the :code:`Manifest` :code:`id`. The :code:`label` will be equivalent to the matching
:code:`mods:subject/mods:geographic` value. Finally, :code:`geometry` will always be a :code:`Point` with the cartographics
in the :code:`coordinates` property in the format of "longitude, latitude".

.. code-block:: json

    {
        "navPlace":
            {
                "id": "https://digital.lib.utk.edu/assemble/manifest/rfta/8/feature-collection/1",
                "type": "FeatureCollection",
                "features": [
                    {
                        "id":"https://digital.lib.utk.edu/assemble/manifest/rfta/8/feature/1",
                        "type":"Feature",
                        "properties":{
                           "label":{
                              "en":[
                                 "Gatlinburg"
                              ]
                           },
                           "manifest": "https://digital.lib.utk.edu/assemble/manifest/rfta/8"
                        },
                        "geometry":{
                           "type":"Point",
                           "coordinates":[
                              -83.51189,
                              35.71453
                           ]
                        }
                    }
                ]
        }
    }