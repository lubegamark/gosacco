# Register your models here.
from django.contrib import admin
from savings.models import Savings, SavingsType, SavingsWithdrawal,SavingsPurchase


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


admin.site.register(Savings, SavingAdmin)
admin.site.register(SavingsType, SavingsTypeAdmin)
admin.site.register(SavingsWithdrawal)
admin.site.register(SavingsPurchase)
