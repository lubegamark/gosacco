# Register your models here.
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from loans.models import LoanType, LoanApplication,  Loan, Security, SecurityArticle, SecuritySavings, SecurityShares


class LoanAdmin(admin.ModelAdmin):
    pass#list_display = ('member','application', 'approval_date', 'amount', 'loan_type')
    #readonly_fields = ('member','application', 'approval_date', 'amount', 'loan_type')
admin.site.register(Loan, LoanAdmin)


class LoanTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoanType, LoanTypeAdmin)


class LoanApplicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoanApplication, LoanApplicationAdmin)

class SecurityChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Security


class SecurityArticleAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)
admin.site.register(SecurityArticle, SecurityArticleAdmin)


class SecuritySavingsAdmin(SecurityChildAdmin):
    list_display = ('__unicode__',)
admin.site.register(SecuritySavings, SecuritySavingsAdmin)


class SecuritySharesAdmin(SecurityChildAdmin):
    list_display = ('__unicode__', 'member')
admin.site.register(SecurityShares, SecuritySharesAdmin)


class SecurityAdmin(PolymorphicParentModelAdmin):
    base_model = Security
    child_models = (
        (SecuritySavings, SecuritySavingsAdmin),
        (SecurityShares, SecuritySharesAdmin),
        (SecurityArticle, SecurityArticleAdmin),
    )
    polymorphic_list = True
admin.site.register(Security, SecurityAdmin)
