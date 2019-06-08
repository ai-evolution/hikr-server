from rest_framework.routers import SimpleRouter
from .viewsets import *
from django.urls import path


urlpatterns = []
r = SimpleRouter()

r.register("tag", TagViewset)
r.register("attraction", AttractionViewset)

urlpatterns.extend(r.urls)