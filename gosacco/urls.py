from django.conf.urls import patterns, include, url
from django.contrib import admin
import notifications

from gosacco import views

authpatterns = patterns('',
                        url(r'token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
                        url(r'token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
                        url(r'registration/', views.AccountView.as_view()),
                        )

apipatterns = patterns('',
                       url(r'^/members/', include('members.member_urls')),
                       url(r'^/groups/', include('members.group_urls')),
                       url(r'^/auth/', include(authpatterns)),
                       # url(r'^/shares/', include('shares.urls')),
                       # url(r'^/savings/', include('savings.urls')),
                       # url(r'^/loans/', include('loans.urls')),

                       )

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api', include(apipatterns)),
                       url('^inbox/notifications/', include(notifications.urls)),

                       )
admin.site.site_header = 'GoSacco'
admin.site.site_title = 'GoSacco'
admin.site.index_title = 'Administration'
