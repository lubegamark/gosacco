from django.conf.urls import patterns, include, url
from django.contrib import admin

from members import views


urlpatterns = patterns('',
                       url(r'^$', views.MemberList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
                       )