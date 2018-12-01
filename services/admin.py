from django.contrib import admin
from django.utils.html import format_html
from django.template.defaultfilters import truncatewords
from django.utils.safestring import mark_safe
from rq import Queue
from posyhubcomng.worker import conn

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

    def save_model(self, request, obj, form, change):
        q = Queue(connection=conn)
        result = q.enqueue(super().save_model, {'request': request, 'obj': obj, 'form':form, 'change':change})