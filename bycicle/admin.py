from django.contrib import admin
from django.db.models import fields
from .models import Bycicle, BycicleCompany
# Register your models here

class BycicleCompanyAdmin(admin.ModelAdmin):
    fields = ["Company name"]

class BycicleAdmin(admin.ModelAdmin):
    fields = ["owner", "Company name"]

admin.site.register(BycicleCompany, BycicleCompanyAdmin)
admin.site.register(Bycicle, BycicleAdmin)
