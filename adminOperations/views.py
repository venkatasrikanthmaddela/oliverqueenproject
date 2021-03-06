from rest_framework.compat import View
from django.shortcuts import render

from adminOperations.models import ProjectUploads


class AdminUserPage(View):
    def get(self, request):
        return render(request, 'adminOperations/adminDashboard.html')


class UploadProjectsPage(View):
    def get(self, request):
        recently_uploaded_projects = ProjectUploads.objects.filter(isDeleted=False).order_by('-createdAt')
        return render(request, 'adminOperations/uploadProjects.html', {"recentUploads": recently_uploaded_projects})


class ImportProjectsPage(View):
    def get(self, request):
        return render(request, 'adminOperations/importProjects.html')


class NewProjectIdeaRequestsPage(View):
    def get(self, request):
        # new_project_idea_requests = NewProjectIdeaUploads.objects.filter(isDeleted=False).order_by('-createdAt')
        return render(request, 'adminOperations/newProjectIdeaRequest.html',
                      {"newProjectIdeaRequests": new_project_idea_requests})

class BulkUploadProjects(View):
    def get(self, request):
        return render(request, 'adminOperations/importProjects.html')