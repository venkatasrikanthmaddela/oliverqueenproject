from django.conf.urls import patterns, include,url

from adminOperations.api_views import UploadProjects, BulkImportProjects

urlpatterns =  patterns("",
                        url(r'upload-project$',UploadProjects.as_view(), name="admin-dashboard"),
                        url(r'delete-project$',UploadProjects.as_view(), name="admin-dashboard"),
                        url(r'update-project$',UploadProjects.as_view(), name="admin-dashboard"),
                        url(r'upload-in-bulk-projects$',BulkImportProjects.as_view())
                        )