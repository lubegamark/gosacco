# Register your models here.
from django.contrib import admin

from shares.models import Shares, ShareType


class ShareAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shares, ShareAdmin)


class ShareTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ShareType, ShareTypeAdmin)

