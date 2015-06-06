from django.conf.urls import patterns, include, url
from django.contrib import admin

apipatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^/members/', include('members.member_urls')),
                       url(r'^/groups/', include('members.group_urls')),
                       url(r'^/shares/', include('shares.urls')),
                       )

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api', include(apipatterns)),
                       )
admin.site.site_header = 'GoSacco'
admin.site.site_title = 'Adminsitration'
admin.site.index_title = 'GoSacco'