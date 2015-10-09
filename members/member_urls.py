from django.conf.urls import patterns, include, url
from django.contrib import admin

from members import views
from shares import views as shares_views
from savings import views as savings_views

urlpatterns = patterns('',
                       url(r'^$', views.MemberList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
                       url(r'^(?P<pk>[0-9]+)/shares$', shares_views.ShareDetail.as_view()),
                       url(r'^(?P<pk>[0-9]+)/shares/purchases$', shares_views.SharePurchaseList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/shares/transfers$', shares_views.ShareTransferList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/savings$', savings_views.SavingsView.as_view()),
                       url(r'^(?P<pk>[0-9]+)/savings/deposits$', savings_views.SavingsDepositView.as_view()),
                       url(r'^(?P<pk>[0-9]+)/savings/withdrawals$', savings_views.SavingsWithdrawalView.as_view()),
                       url(r'^(?P<pk>[0-9]+)/loans$', ),
                       url(r'^(?P<pk>[0-9]+)/loans/applications$', ),
                       url(r'^(?P<pk>[0-9]+)/loans/securities$', ),
                       )