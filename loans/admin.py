# Register your models here.
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from loans.models import SecuritySavings, LoanRuleShares, LoanRuleSavings, LoanRuleOther, SecurityGuarantor
from loans.models import LoanType, LoanApplication, SecurityArticle, Loan, Security, SecurityShares


class LoanAdmin(admin.ModelAdmin):
    list_display = ('member', 'application', 'approval_date', 'amount', 'payment_period', 'loan_type')
    list_filter = ['approval_date', 'payment_period', 'loan_type']
    search_fields = ['loan_type', 'member']


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


class SecurityChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Security


class SecurityArticleAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)


class SecuritySharesAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)


class SecuritySavingsAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)


class SecurityGuarantorAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)


class SecurityAdmin(PolymorphicParentModelAdmin):
    base_model = Security
    child_models = (
        (SecuritySavings, SecuritySavingsAdmin),
        (SecurityShares, SecuritySharesAdmin),
        (SecurityArticle, SecurityArticleAdmin),
        (SecurityGuarantor, SecurityGuarantorAdmin),
    )

    polymorphic_list = True
    list_display = ('__unicode__',)


class SecuritySavingsInline(admin.StackedInline):
    model = SecuritySavings
    extra = 0
    exclude = ('loan',)


class SecuritySharesInline(admin.StackedInline):
    model = SecurityShares
    extra = 0
    exclude = ('loan',)


class SecurityArticleInline(admin.StackedInline):
    model = SecurityArticle
    extra = 0
    exclude = ('loan',)


class SecurityGuarantorInline(admin.StackedInline):
    model = SecurityGuarantor
    extra = 0
    exclude = ('loan',)


class LoanApplicationAdmin(admin.ModelAdmin):
    fields = ['application_number', 'member', 'amount', 'purpose', 'payment_period', 'loan_type', 'status',
              'security_details', ]
    list_display = ('member', 'application_date', 'amount', 'payment_period', 'status')
    list_filter = ['application_date', 'payment_period']
    search_fields = ['member']
    inlines = [SecuritySharesInline, SecuritySavingsInline, SecurityArticleInline, SecurityGuarantorInline]


admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanType, LoanTypeAdmin)
admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(SecurityArticle, SecurityArticleAdmin)
admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityShares, SecuritySharesAdmin)
admin.site.register(SecuritySavings, SecuritySavingsAdmin)
admin.site.register(SecurityGuarantor, SecurityGuarantorAdmin)
