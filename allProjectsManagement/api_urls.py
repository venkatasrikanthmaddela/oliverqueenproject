from django.conf.urls import patterns, url

from allProjectsManagement.api_views import getAllActiveProjects

urlpatterns = patterns("",
                       url('^get-projects$', getAllActiveProjects.as_view())

                     )