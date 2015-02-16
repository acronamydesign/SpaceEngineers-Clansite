from django.conf.urls import patterns, include, url
from django.contrib import admin
import pybb.views as BBOverides
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'SpaceEngineers_Clansite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
