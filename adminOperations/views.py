from rest_framework.compat import View
from django.shortcuts import render

class AdminUserPage(View):
    def get(self, request):
        return render(request, 'adminOperations/adminDashboard.html')

class UploadProjectsPage(View):
    def get(self,request):
        return render(request, 'adminOperations/uploadProjects.html')
