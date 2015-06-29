# Register your models here.
from django.contrib import admin

from savings.models import Savings, SavingsType, SavingsWithdrawal, SavingsPurchase


class SavingsAdmin(admin.ModelAdmin):
    list_display = ('member', 'savings_type', 'amount', 'date')
    readonly_fields = ('member', 'savings_type', 'amount', 'date')
admin.site.register(Savings, SavingsAdmin)


class SavingsTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(SavingsType, SavingsTypeAdmin)


class SavingsWithdrawalAdmin(admin.ModelAdmin):
    list_display = ('member', 'savings_type', 'amount', 'date')

    def save_model(self, request, obj, form, change):
        SavingsWithdrawal.withdraw_savings(obj.member, obj.savings_type, obj.amount)

admin.site.register(SavingsWithdrawal, SavingsWithdrawalAdmin)


class SavingsPurchaseAdmin(admin.ModelAdmin):
    list_display = ('member', 'savings_type', 'amount', 'date')

    def save_model(self, request, obj, form, change):
        SavingsPurchase.make_savings(obj.member, obj.savings_type, obj.amount)

admin.site.register(SavingsPurchase, SavingsPurchaseAdmin)