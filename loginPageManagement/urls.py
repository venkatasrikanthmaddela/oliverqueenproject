from django.conf.urls import patterns, include, url
from loginPageManagement.views import LoginPage

urlpatterns = patterns('',
   url(r'login', LoginPage, name='login-page'),
)