from django.conf.urls import patterns, include, url
from django.contrib import admin

from members import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^loans/$', views.MemberList.as_view()),
                       #url(r'^members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
                       #url(r'^groups/$', views.GroupList.as_view()),
                       #url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),
                       #url(r'^groups/(?P<pk>[0-9]+)/members$', views.GroupMember.as_view()),
                       #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )


