from django.conf.urls import patterns, include, url
from django.contrib import admin
from Sacco.views import member_detail, member_list, group_detail, group_list

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sacco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/members/$', member_list),
    url(r'^apimembers/(?P<pk>[0-9]+)/$', member_detail),
    url(r'^api/groups/$', group_list),
    url(r'^api/groups/(?P<pk>[0-9]+)/$', group_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
