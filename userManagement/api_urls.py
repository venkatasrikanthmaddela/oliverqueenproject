from django.conf.urls import patterns, include, url
from loginPageManagement.views import LoginPage,NewProjectIdeaPost
from userManagement.api_views import loginUser, signUpUser, logoutUser

urlpatterns = patterns('',
   url('^login', loginUser.as_view()),
   url('logout',logoutUser, name='log-out'),
   url('signup/(\w+)', signUpUser.as_view()),
)
