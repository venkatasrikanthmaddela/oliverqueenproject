from django.conf.urls import patterns, include, url
from loginPageManagement.views import HomePage, test_home, search_project, newprojectIdea
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

landing_page_urls = patterns('',
                             url(r'^user-action/', include('loginPageManagement.urls')),
                             )

admin_page_urls = patterns('',
                           url(r'admin/', include('adminOperations.urls')),
                           url(r'api/admin/', include('adminOperations.api_urls')),
                           # url(r'api/student/', include('loginPageManagement.api_urls')),
                           url(r'api/admin/',include('adminOperations.api_urls'))
                           )

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'pmproject.views.home', name='home'),
                       # url(r'^pmproject/', include('pmproject.foo.urls')),
                       url(r'^$', HomePage, name='home-page'),
                       url(r'^test-home$', test_home),
                       url(r'^search-project', search_project, name="search-project"),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )

login_pattern_urls = patterns('',
                          url(r'^account/api/', include('userManagement.api_urls')),
                          )

new_project_idea_urls = patterns('',
                                 url(r'new-project-idea', include('newProjectIdeaManagement.urls')),
                                 url(r'api/new-project-idea/', include('newProjectIdeaManagement.api_urls'))
                                 )

user_dashboard_urls = patterns('',
                               url(r'user-action/my-account/', include('userDashboardManagement.urls')),
                               )

all_projects_urls = patterns('',
                             url(r'api/projects/', include('allProjectsManagement.api_urls')),
                             )

urlpatterns += landing_page_urls
urlpatterns += admin_page_urls
urlpatterns += login_pattern_urls
urlpatterns += new_project_idea_urls
urlpatterns += user_dashboard_urls
urlpatterns += all_projects_urls