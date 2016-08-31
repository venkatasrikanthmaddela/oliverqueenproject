from django.conf.urls import patterns, include, url

from adminOperations.views import AdminUserPage, UploadProjectsPage, ImportProjectsPage, NewProjectIdeaRequestsPage

urlpatterns = patterns("",
                       url(r'home', AdminUserPage.as_view(), name="admin-dashboard"),
                       url(r'upload-projects', UploadProjectsPage.as_view(), name="upload-projects"),
                       url(r'import-projects', ImportProjectsPage.as_view(), name="import-projects"),
                       url(r'new-projects-idea-request', NewProjectIdeaRequestsPage.as_view(),
                           name="new-project-idea-requests"),
                       url(r'delete-new-project-idea-request$', NewProjectIdeaRequestsPage.as_view(),
                           name="admin-dashboard")
                       )