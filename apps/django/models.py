from django.contrib.gis.db import models


class ManagementMixin(models.Model):

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u"Created"
    )

    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name=u"Updated"
    )

    class Meta:
        abstract = True
