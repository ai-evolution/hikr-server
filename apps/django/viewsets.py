from rest_framework import viewsets


__all__ = [
    'MySerializerViewSet',
]


class MySerializerViewSet(viewsets.ModelViewSet):
    serializer_classes = {}

    def get_serializer_class(self):
        """ Return the class to use for serializer w.r.t to the request method."""

        try:
            return self.serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(MySerializerViewSet, self).get_serializer_class()
