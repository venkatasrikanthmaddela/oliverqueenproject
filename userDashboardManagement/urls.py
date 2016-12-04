from django.conf.urls import patterns, include, url

from userDashboardManagement.views import userDashboard

urlpatterns = patterns('',
                       url(r'', userDashboard, name="my-account"),
                       )