from django.shortcuts import render
from rest_framework.compat import View


class LoginPage(View):
    def get(self, request):
        return render(request, "landingPageManagement/login.html")


class HomePage(View):
   def get(self, request):
       return render(request, 'landingPageManagement/home.html')