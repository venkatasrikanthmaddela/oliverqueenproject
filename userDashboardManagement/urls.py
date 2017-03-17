from django.conf.urls import patterns, include, url

from userDashboardManagement.views import userDashboard, seeProjectRequests, seeProjectIdeas

urlpatterns = patterns('',
                       # url(r'see-project-requests',seeProjectRequests, name='see-project-requests'),
                       url(r'^see-project-ideas$', seeProjectIdeas, name="see-project-ideas"),
                       url(r'', userDashboard, name="my-account")
                       )