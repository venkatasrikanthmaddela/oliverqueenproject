from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


landing_page_urls = patterns('',
          url(r'home/', include('landingPageManagement.urls')),
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmproject.views.home', name='home'),
    # url(r'^pmproject/', include('pmproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += landing_page_urls