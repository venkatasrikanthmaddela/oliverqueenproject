from django.conf.urls import patterns, include, url
from landingPageManagement.views import *

urlpatterns = patterns('',
   url(r'login', LoginPage.as_view(), name='login-page'),
   url(r'', HomePage.as_view(), name='home-page')
)