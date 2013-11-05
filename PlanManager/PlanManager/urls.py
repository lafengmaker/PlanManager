from django.conf.urls import patterns, include, url
from settings import STATICFILES_DIRS
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'PlanManager.views.index', name='home'),
     (r'^css/(?P<path>.*)$','django.views.static.serve',
                         {'document_root':STATICFILES_DIRS[0]+'/css'}),
    (r'^js/(?P<path>.*)$','django.views.static.serve',
                         {'document_root':STATICFILES_DIRS[0]+'/js'}),
     (r'^images/(?P<path>.*)$','django.views.static.serve',
                         {'document_root':STATICFILES_DIRS[0]+'/images'}),
     (r'^showimg/(?P<path>.*)$','django.views.static.serve',
                         {'document_root':STATICFILES_DIRS[0]+'/showimg'}),
     url(r'^blog/images/$', 'Blog.views.images', name='images'),
      url(r'^blog/turn90/$', 'Blog.views.turn90', name='turn90'),
    # url(r'^PlanManager/', include('PlanManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
