# Register your models here.
from django.contrib import admin

from savings.models import Saving, SavingsType


class SavingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Saving, SavingAdmin)


class SavingsTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(SavingsType, SavingsTypeAdmin)