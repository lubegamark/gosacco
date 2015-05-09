from django.conf.urls import patterns, include, url
from django.contrib import admin

apipatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^/', include('members.urls')),
                       #url(r'^/', include('members.urls')),
                       )

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api', include(apipatterns)),
                       )