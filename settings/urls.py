from django.conf.urls import patterns, include, url
from django.contrib import admin
address = ''
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pet/submit/','pet.views.submit'),
    url(r'^pet/like/','pet.views.like'),
    url(r'^pet/export/','pet.views.export'),
    url(r'^pet/getUserInformation/','pet.views.getUserInformation'),
    url(r'^portal/update_access_token/','portal.views.update_access_token'),
    url(r'^portal/wxconfig/','portal.views.wxconfig'),
)
