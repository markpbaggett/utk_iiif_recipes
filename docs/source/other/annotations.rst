Annotations
===========

Creating an Annotation that highlights a region of Media
--------------------------------------------------------

Following guidelines from the `W3C Web Annotations <https://www.w3.org/TR/annotation-model/>`_ model
and the `presentation v3 <https://iiif.io/api/presentation/3.0/#b-example-manifest-response>`_ specifications, a valid annotation
in presentation v3 should look like this:

.. literalinclude:: ../../../raw_manifests/galston_696.json
    :language: json
    :linenos:
    :lines: 162-180

The `AnnotationPage` cannot have a label and the value of `annotations.items.[#].body.type` must be valid towards the
`W3C Web Annotations <https://www.w3.org/TR/annotation-model/>`_ model.

The `annotations` section should be in the top level `items` section as a peer to `id`, `type`, `width`, `height`, etc.

.. literalinclude:: ../../../raw_manifests/galston_696.json
    :language: json
    :linenos:
    :lines: 123-134, 161, 162, 180-182