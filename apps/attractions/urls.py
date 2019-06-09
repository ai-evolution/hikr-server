from rest_framework.routers import SimpleRouter
from .viewsets import *
from .views import YandexMapWebView
from django.urls import path


urlpatterns = [
    path('webview/', YandexMapWebView.as_view(), name='webview')
]

r = SimpleRouter()

r.register("tag", TagViewset)
r.register("attraction", AttractionViewset)

urlpatterns.extend(r.urls)