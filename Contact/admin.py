from django.contrib import admin
from .models import CompanyAddress, CompanyDetail


class AddressInline(admin.TabularInline):
    model = CompanyAddress


class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'email']
    inlines = [AddressInline]

admin.site.register(CompanyDetail, CompanyDetailAdmin)