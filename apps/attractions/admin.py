from django.contrib import admin
from .models import *


class AttractionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'node_id', 'name', 'address',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'tags',
    )


class CategoryInlineAdmin(admin.StackedInline):
    model = Category


class TagAdmin(admin.ModelAdmin):
    inlines = (
        CategoryInlineAdmin,
    )

    search_fields = (
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Attraction, AttractionAdmin)
