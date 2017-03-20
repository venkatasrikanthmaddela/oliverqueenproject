from rest_framework.views import APIView
from rest_framework.response import Response

from adminOperations.models import ProjectUploads


class getAllActiveProjects(APIView):
    def get(self, request):
        active_projects_data = list()
        all_open_projects = ProjectUploads.objects.filter(isDeleted=False).order_by('-createdAt')
        for each_project_object in all_open_projects:
            project_as_json = {
                "projectId":each_project_object.project_id,
                "projectTitle": each_project_object.project_title,
                "projectStream":each_project_object.target_stream,
                "projectFramework":each_project_object.project_frame_work,
                "IeePaper":each_project_object.iee_paper,
                "projectAbstract":each_project_object.abstract,
                "projectProvider":each_project_object.project_provider,
                "projectCode":each_project_object.project_code,
                "uploadedUser":each_project_object.uploaded_user,
                "project_pk":each_project_object.pk
            }
            active_projects_data.append(project_as_json)
        return Response(active_projects_data,200)
