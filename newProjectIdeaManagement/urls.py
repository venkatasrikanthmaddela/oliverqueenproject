from django.conf.urls import patterns, include, url

from newProjectIdeaManagement.views import projectIdeaHomePage, projectIdeaSuccessPage

urlpatterns = patterns('',
                       url('^$', projectIdeaHomePage, name='new-project-idea'),
                       url('success', projectIdeaSuccessPage, name='new-project-idea-success'),
                       )