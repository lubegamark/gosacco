# Register your models here.
from django.contrib import admin
from savings.models import Savings, SavingsType, SavingsWithdrawal, SavingsDeposit


class SavingsAdmin(admin.ModelAdmin):
    list_display = ('member', 'savings_type', 'amount', 'date')
    readonly_fields = ('member', 'savings_type', 'amount', 'date')
# # admin.site.register(Savings, SavingsAdmin)


class SavingsTypeAdmin(admin.ModelAdmin):
    pass
# # admin.site.register(SavingsType, SavingsTypeAdmin)


class SavingsWithdrawalAdmin(admin.ModelAdmin):
    list_display = ('member', 'savings_type', 'amount', 'date')

    def save_model(self, request, obj, form, change):
        SavingsWithdrawal.withdraw_savings(obj.member, obj.savings_type, obj.amount)

# # admin.site.register(SavingsWithdrawal, SavingsWithdrawalAdmin)


class savingsdepositAdmin(admin.ModelAdmin):
    list_display = ('member', 'savings_type', 'amount', 'date')

    def save_model(self, request, obj, form, change):
        SavingsDeposit.make_savings(obj.member, obj.savings_type, obj.amount)

# # admin.site.register(SavingsDeposit, savingsdepositAdmin)

from savings.models import Savings, SavingsType, SavingsWithdrawal,SavingsDeposit


class SavingAdmin(admin.ModelAdmin):
	change_list_template = "admin/change_list_filter_sidebar.html"
	change_list_filter_template = "admin/filter_listing.html"

	list_display=('member_name','savings_type','amount','date')
	list_filter=['savings_type','date','amount']
	search_fields=[]




class SavingsTypeAdmin(admin.ModelAdmin):
	change_list_template = "admin/change_list_filter_sidebar.html"
	change_list_filter_template = "admin/filter_listing.html"

	list_display =('name','category','compulsory','interval','minimum_amount','maximum_amount','interest_rate')
	list_filter = ['name']
	search_fields =['name','category']


admin.site.register(Savings, SavingsAdmin)
admin.site.register(SavingsType, SavingsTypeAdmin)
admin.site.register(SavingsWithdrawal, SavingsWithdrawalAdmin)
admin.site.register(SavingsDeposit, savingsdepositAdmin)
