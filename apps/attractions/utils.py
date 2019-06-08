import requests

def geocode(address):
    print(address)
    r = requests.get("https://geocode-maps.yandex.ru/1.x", params={
        "geocode": address,
        "apikey": "6fcc7358-c699-490c-827b-621db017f699",
        "format": "json"
    })
    r.raise_for_status()
    return r.json().get('response').get('GeoObjectCollection').get('featureMember')[0].get('GeoObject').get('Point').get('pos').split(' ')