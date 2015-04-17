# Register your models here.
from django.contrib import admin

from shares.models import Share, ShareType


class ShareAdmin(admin.ModelAdmin):
    pass


admin.site.register(Share, ShareAdmin)


class ShareTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShareType, ShareTypeAdmin)

