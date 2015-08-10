# Register your models here.
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from loans.models import LoanType, LoanApplication,  Loan, Security, SecurityArticle, SecuritySavings, SecurityShares

<<<<<<< HEAD
=======
from loans.models import LoanType, LoanApplication, SecurityArticle, Loan, Security, SecurityShares
>>>>>>> frontend

class LoanAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    list_display=('member','application','approval_date','amount','payment_period','type')
    list_filter =['approval_date','payment_period','type']
    search_fields=['type','member']



class LoanTypeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    pass

admin.site.register(LoanType, LoanTypeAdmin)


class LoanApplicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(LoanApplication, LoanApplicationAdmin)
=======
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    list_display = ('name','interest','interest_period','minimum_amount','maximum_amount','minimum_share','minimum_savings')
    list_filter=['interest_period','minimum_membership_period']
    search_fields=['name']


class LoanApplicationAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display=('member_name','application_number','application_date','amount','type','status')
    list_filter=['application_date','type','status']
    search_fields =['application_number','type','status']

>>>>>>> frontend

class SecurityChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Security



class SecurityArticleAdmin(SecurityChildAdmin):
    list_display = ('__unicode__', 'member')

<<<<<<< HEAD
admin.site.register(SecurityArticle, SecurityArticleAdmin)




class SecuritySharesAdmin(SecurityChildAdmin):
    list_display = ('__unicode__', 'member')

admin.site.register(SecurityShares, SecuritySharesAdmin)

class SecuritySavingsAdmin(SecurityChildAdmin):
    list_display = ('__unicode__', 'member')

admin.site.register(SecuritySavings, SecuritySavingsAdmin)


class SecurityAdmin(PolymorphicParentModelAdmin):
    base_model = Security
    child_models = (
        (SecuritySavings, SecuritySavingsAdmin),
        (SecurityShares, SecuritySharesAdmin),
        (SecurityArticle, SecurityArticleAdmin),
    )

    polymorphic_list = True
    list_display = ('__unicode__', 'member')

=======
class SecurityArticleAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display=('name','owner','type','identification_type','attached_to_loan','security')
    list_filter = ['type','identification_type','security']
    search_fields=['name','type','owner','identification_type','security']



class SecurityAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display =('security_type','attached_to_loan')
    list_filter =['attached_to_loan']
    search_fields=['security_type']

class SecuritySharesAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display=('share_type','number_of_shares','value_of_shares','security')
    list_filter=['share_type','security']
    search_fields=['share_type','security']


admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanType, LoanTypeAdmin)
admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(SecurityArticle, SecurityArticleAdmin)
>>>>>>> frontend
admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityShares, SecuritySharesAdmin)
