from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin
from django.conf import settings



admin.autodiscover()

urlpatterns = patterns('',
                       
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
)


#urlpatterns += patterns('django.contrib.auth.views',               
#
#    url(r'^login/$', 'login', {'template_name': 'users/login.html',}, name='login'),  
#    url(r'^logout/$', 'logout', {'template_name': 'users/login.html'},name='logout'),
#        
#
#)

if settings.SERVE_MEDIA:
    
    urlpatterns += staticfiles_urlpatterns()
