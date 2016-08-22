from rest_framework.views import APIView

from rest_framework.response import Response

from adminOperations.models import ProjectUploads


class UploadProjects(APIView):
    def post(self, request):
        project_data = request.DATA
        projectTitle = project_data.get("projectTitle")
        projectFramework = project_data.get("projectFramework")
        targetStream = project_data.get("targetStream")
        ieePaper = True if project_data.get("ieePaper") == "available" else False
        projectAbstract = project_data.get("projectAbstract")
        project_data_object = ProjectUploads(project_title=projectTitle, project_frame_work=projectFramework, target_stream=targetStream,
                       iee_paper=ieePaper, abstract=projectAbstract, uploaded_user="srikanth")
        project_data_object.save()
        return Response({'result':'success'}, 200)

    def delete(self, request):
        delete_data = request.DATA
        project_data = ProjectUploads.objects.get(id=delete_data.get("orderId"))
        project_data.isDeleted = True
        project_data.save()
        return Response({'result':'success'}, 200)

    def put(self, request):
        update_form_data = request.DATA
        project_data = ProjectUploads.objects.get(id=update_form_data.get("projectId"))
        project_data.project_title = update_form_data.get("projectTitle")
        project_data.project_frame_work = update_form_data.get("projectFramework")
        project_data.target_stream = update_form_data.get("targetStream")
        project_data.iee_paper = True if update_form_data.get("ieePaper") == "available" else False
        project_data.abstract = update_form_data.get("projectAbstract")
        project_data.save()
        return Response({"result":"success"}, 200)