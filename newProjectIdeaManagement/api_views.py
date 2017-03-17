from rest_framework.views import APIView
from rest_framework.response import Response
from newProjectIdeaManagement.models import NewProjectIdea
from userManagement.models import PmUser


class saveNewProject(APIView):
    def post(self, request):
        new_project_data = request.DATA
        user_details = PmUser.objects.get(email=request.user.email)
        project_data = NewProjectIdea(customerId=user_details, customerName=new_project_data.get("customerName"),
                                      customerEmail=new_project_data.get("customerEmail"), customerMobile=new_project_data.get("customerMobile"),
                                      projectTitle=new_project_data.get("projectTitle"), projectStream=new_project_data.get("targetStream"),
                                      projectFramework=new_project_data.get("projectFramework"), projectDescription= new_project_data.get("projectDescription"),
                                      additionalData=dict(new_project_data))
        project_data.save()
        return Response({"success":"data saved successfully"}, 200)