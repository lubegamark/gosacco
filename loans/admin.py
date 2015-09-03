# Register your models here.
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from loans.models import LoanType, LoanApplication,  Loan, Security, SecurityArticle, SecuritySavings, SecurityShares, \
     LoanRuleShares, LoanRuleSavings, LoanRuleOther
from loans.models import LoanType, LoanApplication, SecurityArticle, Loan, Security, SecurityShares

class LoanAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    list_display=('member','application','approval_date','amount','payment_period','loan_type')
    list_filter =['approval_date','payment_period','loan_type']
    search_fields=['loan_type','member']

class LoanRuleSharesAdmin(admin.TabularInline):
    model = LoanRuleShares
    extra = 0


class LoanRuleSavingsAdmin(admin.TabularInline):
    model = LoanRuleSavings
    extra = 0


class LoanRuleOtherAdmin(admin.TabularInline):
    model = LoanRuleOther
    extra = 0


class LoanTypeAdmin(admin.ModelAdmin):
    inlines = [LoanRuleSharesAdmin, LoanRuleSavingsAdmin, LoanRuleOtherAdmin]

# admin.site.register(LoanType, LoanTypeAdmin)





# class LoanApplicationAdmin(admin.ModelAdmin):
    # change_list_template = "admin/change_list_filter_sidebar.html"
    # change_list_filter_template = "admin/filter_listing.html"
    # list_display=('member_name','application_number','application_date','amount','type','status')
    # list_filter=['application_date','type','status']
    # search_fields =['application_number','type','status']



class SecurityChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Security



class SecurityArticleAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)


# admin.site.register(SecurityArticle, SecurityArticleAdmin)




class SecuritySharesAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)

# admin.site.register(SecurityShares, SecuritySharesAdmin)

class SecuritySavingsAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)

# admin.site.register(SecuritySavings, SecuritySavingsAdmin)


class SecurityAdmin(PolymorphicParentModelAdmin):
    base_model = Security
    child_models = (
        (SecuritySavings, SecuritySavingsAdmin),
        (SecurityShares, SecuritySharesAdmin),
        (SecurityArticle, SecurityArticleAdmin),
    )

    polymorphic_list = True
    list_display = ('__unicode__',)


class SecurityArticleAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display =('name','type','identification_type','identification')
    list_filter = ['type','identification_type']
    search_fields =['name','type']


class SecuritySharesAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display=('share_type','number_of_shares','value_of_shares')
    list_filter=['share_type']
    search_fields=['share_type']


class SecuritySavingsInline(admin.StackedInline):
    model = SecuritySavings
    extra = 0


class SecuritySharesInline(admin.StackedInline):
    model = SecurityShares
    extra = 0


class SecurityArticleInline(admin.StackedInline):
    model = SecurityArticle
    extra = 0


class LoanApplicationAdmin(admin.ModelAdmin):
    fields = ['application_number', 'member', 'amount', 'purpose', 'payment_period', 'loan_type', 'status', 'security_details',]

# admin.site.register(LoanApplication, LoanApplicationAdmin)

    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    list_display = ('member','application_date','amount','payment_period','status')
    list_filter=['application_date','payment_period']
    search_fields=['member']
    inlines = [SecuritySharesInline, SecuritySavingsInline, SecurityArticleInline]

admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanType, LoanTypeAdmin)
admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(SecurityArticle, SecurityArticleAdmin)
admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityShares, SecuritySharesAdmin)
admin.site.register(SecuritySavings, SecuritySavingsAdmin)
