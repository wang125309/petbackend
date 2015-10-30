from django.conf.urls import patterns, include, url
from django.contrib import admin
address = ''
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^'+address+'/pet/submit/','running.views.submit'),
    url(r'^'+address+'/pet/export/','running.views.export'),
    url(r'^'+address+'/portal/update_access_token/','portal.views.update_access_token'),
    url(r'^'+address+'/portal/wxconfig/','portal.views.wxconfig'),
)
