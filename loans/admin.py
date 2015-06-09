# Register your models here.
from django.contrib import admin

from loans.models import LoanType, LoanApplication, SecurityArticle, Loan, Security

class LoanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Loan, LoanAdmin)


class LoanTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoanType, LoanTypeAdmin)


class LoanApplicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoanApplication, LoanApplicationAdmin)


class SecurityArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(SecurityArticle, SecurityArticleAdmin)


class SecurityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Security, SecurityAdmin)
