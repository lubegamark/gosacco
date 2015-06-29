# Register your models here.
from django.contrib import admin

from shares.models import Shares, ShareType, SharePurchase, ShareTransfer


class ShareAdmin(admin.ModelAdmin):
    list_display = ('member', 'share_type', 'number_of_shares', 'date')
    search_fields = ('member', 'share_type')
    readonly_fields = ('member', 'share_type', 'number_of_shares', 'date')
admin.site.register(Shares, ShareAdmin)


class SharePurchaseAdmin(admin.ModelAdmin):
    list_display = ('member', 'share_type', 'number_of_shares', 'date')
    search_fields = ('member', 'share_type', 'date')
    exclude = ('current_share_price',)

    def save_model(self, request, obj, form, change):
        SharePurchase.issue_shares(obj.member, obj.number_of_shares, obj.share_type)
admin.site.register(SharePurchase, SharePurchaseAdmin)


class ShareTransferAdmin(admin.ModelAdmin):
    list_display = ('seller', 'buyer', 'share_type', 'number_of_shares', 'date')
    exclude = ('current_share_price',)

    def save_model(self, request, obj, form, change):
        ShareTransfer.transfer_shares(obj.seller, obj.buyer, obj.number_of_shares, obj.share_type)

admin.site.register(ShareTransfer, ShareTransferAdmin)


class ShareTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ShareType, ShareTypeAdmin)

