from django.conf.urls import patterns, include,url

from adminOperations.views import AdminUserPage, UploadProjectsPage

urlpatterns =  patterns("",
                        url(r'home',AdminUserPage.as_view(), name="admin-dashboard"),
                        url(r'upload-projects', UploadProjectsPage.as_view(), name="upload-projects")
                        )