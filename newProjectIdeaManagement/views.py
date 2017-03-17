from django.http import request
from django.shortcuts import render

def projectIdeaHomePage(request):
        return render(request, 'newProjectIdeaManagement/newProjectIdea.html', {"request":request})

def projectIdeaSuccessPage(request):
    return render(request, 'newProjectIdeaManagement/projectIdeaSubmitSucess.html', {"request":request})