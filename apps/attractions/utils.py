import requests
from django.conf import settings

def geocode(address):
    print(address)
    r = requests.get("https://geocode-maps.yandex.ru/1.x", params={
        "geocode": address,
        "apikey": settings.YANDEX_API_KEY,
        "format": "json"
    })
    r.raise_for_status()
    return r.json().get('response').get('GeoObjectCollection').get('featureMember')[0].get('GeoObject').get('Point').get('pos').split(' ')