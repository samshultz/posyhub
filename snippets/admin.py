from django.contrib import admin
from .models import SocialMediaLinks, NewSocialMediaLink, SupportEmail, SupportEmails


class NewSocialMediaLinkInline(admin.TabularInline):
    model = NewSocialMediaLink
    extra = 1


@admin.register(SocialMediaLinks)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    inlines = [NewSocialMediaLinkInline,]



class SupportEmailInline(admin.TabularInline):
    model = SupportEmail
    extra = 1


@admin.register(SupportEmails)
class SupportEmailAdmin(admin.ModelAdmin):
    inlines = [SupportEmailInline,]