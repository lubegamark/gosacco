# Register your models here.
from django.contrib import admin

from savings.models import Savings, SavingsType


class SavingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Savings, SavingAdmin)


class SavingsTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(SavingsType, SavingsTypeAdmin)