from django.conf.urls import patterns, include, url
from django.contrib import admin

from members import views
from shares import views as shares_views

urlpatterns = patterns('',
                       url(r'^$', views.MemberList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
                       url(r'^(?P<pk>[0-9]+)/shares$', shares_views.ShareDetail.as_view()),
                       url(r'^(?P<pk>[0-9]+)/sharepurchases$', shares_views.SharePurchaseList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/sharetransfers$', shares_views.ShareTransferList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/savings$', shares_views.ShareDetail.as_view()),
                       url(r'^(?P<pk>[0-9]+)/sharepurchases$', shares_views.SharePurchaseList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/sharetransfers$', shares_views.ShareTransferList.as_view()),

                       )