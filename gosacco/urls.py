from django.conf.urls import patterns, include, url
from django.contrib import admin
from gosacco import views


authpatterns = patterns('',
                       #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
                       url(r'token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
                       url(r'registration/', views.AccountView.as_view()),
                       )

apipatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^/members/', include('members.member_urls')),
                       url(r'^/groups/', include('members.group_urls')),
                       #url(r'^/shares/', include('shares.urls')),
                       #url(r'^/savings/', include('savings.urls')),
                       url(r'^/auth/', include(authpatterns)),
                       #url(r'^/loans/', include('loans.urls')),

                       )


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'members.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api', include(apipatterns)),



                       )
admin.site.site_header = 'GoSacco'
admin.site.site_title = 'Adminsitration'
admin.site.index_title = 'GoSacco'
