__author__ = 'leona'

from django.conf.urls import patterns, include, url
from django.contrib import admin

import views


urlpatterns = patterns('',

                       # url(r'^(?P<member_pk>[0-9]+)/$', views.ShareList.as_view()),
                       url(r'^loanlist', views.LoanApplicationList.as_view()),
                       # url(r'^savingscreate',views.SavingsCreate.as_view()),
                       # url(r'^savingsdetail/(?P<pk>[0-9]+)/', views.SavingsDetail.as_view()),
                       # url(r'^savingstypelist/$', views.SavingsTypeList.as_view()),
                       # url(r'^savingstypedetail/(?P<pk>[0-9]+)/', views.SavingsTypeDetail.as_view()),
                       # url(r'^savingswithdrawlist', views.SavingsWithdrawList.as_view()),
                       # url(r'^savingswithdrawdetail/(?P<pk>[0-9]+)/', views.SavingsWithdrawDetail.as_view()),
                       # url(r'^savingspurchaselist/$', views.SavingsPurchaseList.as_view()),
                       # url(r'^savingspurchasedetail/(?P<pk>[0-9]+)/', views.SavingsPurchaseDetail.as_view()),

                       )


