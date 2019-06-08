from rest_framework import authentication
from django.contrib.auth.models import User


class DeviceAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.headers.get('Deviceid'), "SFADA")

        username = request.headers.get('Deviceid')
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create(username=username)
        return (user, None)