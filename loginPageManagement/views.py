from django.shortcuts import render

from adminOperations.models import ProjectUploads


def HomePage(request):
    return render(request, 'loginPageManagement/home.html', {"request":request})


def LoginPage(request):
    return render(request, "loginPageManagement/newLogin.html")


def test_home(request):
    return render(request, "newBase.html")


def search_project(request):
    all_open_projects = ProjectUploads.objects.filter(isDeleted=False).order_by('-createdAt')
    return render(request, "allProjectsManagement/searchProjects.html", {"allProjects": all_open_projects})


def newprojectIdea(request):
    return render(request, 'loginPageManagement/newProjectIdea.html')


def NewProjectIdeaPost(request):
    def get(self, request):
        return render(request, 'loginPageManagement/newProjectIdea.html')
