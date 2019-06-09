from django.core.management.base import BaseCommand, CommandError
from lxml import etree as et
from apps.attractions.models import *
from django.contrib.gis.geos import Point


FILTERS = [
    'tourism', 'amenity', 'building', 'shop', 'sport', 'leisure', 'heritage'
]

IGNORE = [
    'website_1', 'opening_hours', 'contact'
]


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('osm', type=str)

    def handle(self, *args, **options):
        osm = options.get('osm')
        parser = et.iterparse(osm, events=('end',))
        tags = {}
        for t in Tag.objects.all():
            tags[t.slug] = t
        categories = {}
        for c in Category.objects.all():
            categories[c.slug] = c
        keys = set()
        for events, elem in parser:
            obj = {}
            if elem.tag == "osm":
                print(elem.attrib)
            if elem.tag == "tag":
                continue

            if elem.tag == "node":

                added = False
                for e in elem:
                    key = e.attrib.get('k')
                    if key in FILTERS:
                        added = True
                    if (key != "name" and key.startswith("name")):
                        continue
                    obj[key] = e.attrib.get('v')
                if not added:
                    elem.clear()
                    continue
                if not obj.get('name'):
                    elem.clear()
                    continue
                try:
                    point = None
                    if elem.attrib.get('lon') and elem.attrib.get('lat'):
                        point = Point(float(elem.attrib.get('lon')), float(elem.attrib.get('lat')))
                    addr = None
                    if obj.get('addr:street') and obj.get('addr:housenumber'):
                        addr = "Санкт-Петербург, {}, {}".format(obj.get('addr:street'), obj.get('addr:housenumber'))
                    #print(obj)
                    if not ((addr or point) and obj.get('name')):
                        elem.clear()
                        continue
                    a = Attraction.objects.create(
                        node_id=int(elem.attrib.get('id')),
                        name=obj.get('name'),
                        point=point,
                        address=addr,
                    )
                except Exception as e:
                    print(e)
                    elem.clear()
                    continue
                print(a)
                for k, v in obj.items():
                    if k in IGNORE:
                        continue
                    tag = tags.get(k)
                    if not tag:
                        tag = Tag.objects.create(name=k, slug=k)
                        tags[k] = tag
                    a.tags.add(tag)
                    category = categories.get(v)
                    if not category:
                        category = Category.objects.create(slug=v, name=v, tag=tag)
                        categories[v] = category
                    a.categories.add(category)
                # obj["id"] =
                #
                # obj["lat"] =
                # obj["lon"] =
                # if 'sport' in obj:
                #     print(obj)
                # if 'amenity' in obj:
                #     #print(obj)
                #     pass
                # if '' in obj:
                #     if obj.get('railway'):
                #         continue

                ## Do some cleaning
                # Get rid of that element
                elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
