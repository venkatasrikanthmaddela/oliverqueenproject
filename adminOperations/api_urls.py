from django.conf.urls import patterns, include,url

from adminOperations.api_views import UploadProjects

urlpatterns =  patterns("",
                        url(r'upload-project-data',UploadProjects.as_view(), name="admin-dashboard")
                        )