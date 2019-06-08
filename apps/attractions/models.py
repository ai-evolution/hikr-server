from django.db import models
from django.contrib.auth.models import User
from googlemaps import Client
from ..django.models import ManagementMixin
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.dispatch import receiver
from .utils import geocode
from ..django.middlewares import get_current_user
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


class Category(ManagementMixin):

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class UserAttraction(ManagementMixin):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    attraction = models.ForeignKey(
        "Attraction",
        on_delete=models.CASCADE,
        related_name="users",
    )

    visited = models.BooleanField(
        default=False,
    )

    liked = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = [['user', 'attraction']]


class Tag(ManagementMixin):

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Attraction(ManagementMixin):

    name = models.CharField(
        max_length=2048,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
    )

    address = models.CharField(
        max_length=2048,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    related = models.ManyToManyField(
        "Attraction",
        null=True,
        blank=True,
    )

    point = models.PointField(
        geography=True,
        null=True,
        blank=True,
    )

    user = models.ManyToManyField(
        User,
        through=UserAttraction,
    )

    tags = models.ManyToManyField(
        Tag,
    )

    @property
    def liked(self):
        ua, _ = UserAttraction.objects.get_or_create(
            user=get_current_user(),
            attraction=self,
        )
        return ua.liked

    @property
    def visit_count(self):
        return self.users.filter(visited=True).count()

    @property
    def like_count(self):
        return self.users.filter(liked=True).count()


    @property
    def state(self):
        user = get_current_user()
        if not user.is_authenticated:
            return UserAttraction()
        ua, _ = UserAttraction.objects.get_or_create(
            user=get_current_user(),
            attraction=self,
        )
        return ua

    def toggle_like(self, user, like):
        ua, _ = UserAttraction.objects.get_or_create(
            user=user,
            attraction=self,
            defaults={
                "liked": like,
            }
        )
        if ua.liked != like:
            ua.liked = like
            ua.save()

    def toggle_visit(self, user, visit):
        ua, _ = UserAttraction.objects.get_or_create(
            user=user,
            attraction=self,
            defaults={
                "visited": visit,
            }
        )
        if ua.liked != visit:
            ua.liked = visit
            ua.save()

    @classmethod
    def search(cls, tags, point):
        print(point)
        print(cls.objects.filter(point__isnull=False).first().point)
        return cls.objects.filter(point__distance_lte=(point, Distance(km=3)))

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Attraction)
def get_coord(sender, instance, added=False, **kwargs):
    if instance.point:
        return
    try:
        x,y  = geocode(instance.address)
        instance.point = Point(float(x), float(y))
    except Exception as e:
        print(e)
