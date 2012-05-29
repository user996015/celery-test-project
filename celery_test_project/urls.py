from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^people/delay/(?P<person_id>\d+)/$', 'people.views.call_celery_delay', name='call-celery-delay'),
)
