from django.contrib import admin

# Register your models here.
from fees.models import Fee, FeeType, FeePayment


#class FeesAdmin(admin.ModelAdmin):
#    pass
#    #list_display = ('member_name', 'share_type', 'number_of_shares', 'date')

#admin.site.register(Fee, FeesAdmin)

#class FeeTypeAdmin(admin.ModelAdmin):
#    list_display = ('name', 'purpose', 'minimum_amount', 'maximum_amount')

#admin.site.register(FeeType, FeeTypeAdmin)


class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'fee_type', 'amount', 'date', 'reason')

admin.site.register(FeePayment, FeePaymentAdmin)