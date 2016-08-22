from django.conf.urls import patterns, include, url
from loginPageManagement.views import HomePage, test_home, search_project
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


landing_page_urls = patterns('',
          url(r'^user-action/', include('loginPageManagement.urls')),
)

admin_page_urls = patterns('',
                           url(r'admin/',include('adminOperations.urls')),
                           url(r'api/admin/', include('adminOperations.api_urls'))
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmproject.views.home', name='home'),
    # url(r'^pmproject/', include('pmproject.foo.urls')),
    url(r'^$', HomePage, name='home-page'),
    url(r'^test-home$', test_home),
    url(r'^search-project', search_project, name="search-project")

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += landing_page_urls
urlpatterns += admin_page_urls