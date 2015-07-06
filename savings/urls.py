__author__ = 'leona'

from django.conf.urls import patterns, include, url
from django.contrib import admin

import views


urlpatterns = patterns('',

                       # url(r'^(?P<member_pk>[0-9]+)/$', views.ShareList.as_view()),
                       url(r'^savings', views.SavingsList.as_view()),
                       # url(r'^sharetype/$', views.ShareTypeList.as_view()),
                       # url(r'^sharetransfer/$', views.ShareTransferList.as_view()),

                       )


