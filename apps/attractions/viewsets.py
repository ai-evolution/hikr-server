from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ..django.auth import DeviceAuthentication
from rest_framework import permissions
from django.contrib.gis.geos import Point


__all__ = [
    'AttractionViewset',
    'TagViewset',
]


class AttractionViewset(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (DeviceAuthentication,)

    def get_queryset(self):
        tags = Tag.objects.filter(id__in=[int(x) for x in self.request.GET.getlist('tag')])
        return Attraction.search(tags=tags, point=Point(60.004532, 30.43344))


    @action(detail=True, methods=["GET"])
    def like(self, request, pk, **kwargs):
        obj = self.get_object()
        obj.toggle_like(self.request.user, True)
        return Response(self.serializer_class(instance=obj).data)

    @action(detail=True, methods=["GET"])
    def dislike(self, request, pk, **kwargs):
        obj = self.get_object()
        obj.toggle_like(self.request.user, False)
        return Response(self.serializer_class(instance=obj).data)

    @action(detail=True, methods=["GET"])
    def visit(self, request, pk, **kwargs):
        obj = self.get_object()
        obj.toggle_visit(self.request.user, True)
        return Response(self.serializer_class(instance=obj).data)

    @action(detail=True, methods=["GET"])
    def unvisit(self, request, pk, **kwargs):
        obj = self.get_object()
        obj.toggle_visit(self.request.user, False)
        return Response(self.serializer_class(instance=obj).data)


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny, )

