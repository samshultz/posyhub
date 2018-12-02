from django.contrib import admin
from django.utils.html import format_html
from django.template.defaultfilters import truncatewords
from django.utils.safestring import mark_safe

import django_rq
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', "display_image", "get_brief_description")
    prepopulated_fields = {'slug': ('name',)}

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src={} height="100" width="100" />'.format(obj.image.url))

    def get_brief_description(self, obj):
        return mark_safe(truncatewords(obj.description, 20))