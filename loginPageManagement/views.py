from django.shortcuts import render


def HomePage(request):
    return render(request, 'loginPageManagement/home.html')

def LoginPage(request):
    return render(request, "loginPageManagement/newLogin.html")

def test_home(request):
    return render(request, "newBase.html")