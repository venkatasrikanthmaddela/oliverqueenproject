from django.shortcuts import render
from django.http import request

def userDashboard(request):
    return render(request, 'userDashboardManagement/userDashboard.html', {"request":request})