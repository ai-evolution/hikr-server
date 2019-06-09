from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ..django.auth import DeviceAuthentication
from rest_framework import permissions
from django.contrib.gis.geos import Point
from django.urls import reverse
from django.utils.http import urlencode

__all__ = [
    'AttractionViewset',
    'TagViewset',
]


class AttractionViewset(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    authentication_classes = (DeviceAuthentication,)
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        tags = Tag.objects.filter(id__in=[int(x) for x in self.request.GET.getlist('tag')])
        x = self.request.GET.get('x')
        y = self.request.GET.get('y')
        if not x or not y:
            return Response(status=400, data="point not specify")
        try:
            point = Point(float(x), float(y))
        except Exception as e:
            print(e)
            return Response(status=400, data=e)
        return Attraction.search(tags=tags, point=point, distance=int(self.request.GET.get('distance', 3)))

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        return Response(status=200, data={
            "url": "{}?{}&{}".format(reverse('api:webview'), "&attraction=".join([str(x.id) for x in qs]),
                                     urlencode({
                                         "y": self.request.GET.get('y'),
                                         "x": self.request.GET.get('x')})),
            "count": qs.count(),
            "objects": self.serializer_class(instance=qs, many=True).data,
        })

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
    queryset = Tag.objects.filter(attention=True)
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny, )

