from django.contrib import admin
from .models import SocialMediaLinks, NewSocialMediaLink


class NewSocialMediaLinkInline(admin.TabularInline):
    model = NewSocialMediaLink
    extra = 1


@admin.register(SocialMediaLinks)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    inlines = [NewSocialMediaLinkInline,]
