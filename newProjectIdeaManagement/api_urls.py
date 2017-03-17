from django.conf.urls import patterns, include, url

from newProjectIdeaManagement.api_views import saveNewProject

urlpatterns = patterns('',
                        url(r'save-project-idea', saveNewProject.as_view(), name="save-new-idea"),
                        )