from django.conf.urls import patterns, include, url
from loginPageManagement.views import LoginPage,NewProjectIdeaPost

urlpatterns = patterns('',
   url(r'login', LoginPage, name='login-page'),
   url(r'new-project-ideas', NewProjectIdeaPost, name="new-project-idea"),
)
