from django.views.generic import TemplateView
from django.conf import settings
from .models import Attraction
from django.contrib.gis.geos import Point
from django.shortcuts import HttpResponse

__all__ = [
    'YandexMapWebView',
]


class YandexMapWebView(TemplateView):
    template_name = 'routes.html'

    def get_context_data(self, **kwargs):
        ids = self.request.GET.getlist('attraction')
        attractions = Attraction.objects.filter(pk__in=[int(x) for x in ids])
        if "x" not in self.request.GET or "y" not in self.request.GET:
            return HttpResponse(status=400)
        start_pos = Point(float(self.request.GET.get('x')), float(self.request.GET.get('y')))

        return {
            "YANDEX_API_KEY": settings.YANDEX_API_KEY,
            "attractions": attractions,
            "start_pos": start_pos,
        }