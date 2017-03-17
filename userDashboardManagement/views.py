from django.shortcuts import render
from django.http import request

from userDashboardManagement.view_utils import get_all_user_activites


def userDashboard(request):
    user_activity_details = get_all_user_activites(request)
    return render(request, 'userDashboardManagement/userDashboard.html', {"request":request, "userDashboardDetails":user_activity_details})


def seeProjectRequests(request):
    return render(request, 'userDashboardManagement/myProjectRequests.html', {})


def seeProjectIdeas(request):
    user_activity_details = get_all_user_activites(request)
    return render(request, 'userDashboardManagement/myProjectIdeas.html', {"request":request, "userActivityDetails": user_activity_details})