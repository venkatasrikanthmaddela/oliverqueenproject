from datetime import datetime
from rest_framework.views import APIView

from rest_framework.response import Response

from xlrd import open_workbook

import django_excel as excel

from adminOperations.constants import BULK_IMPORT_COLS
from adminOperations.models import ProjectUploads
from adminOperations.utils import ExcelValidations



class UploadProjects(APIView):
    def post(self, request):
        project_data = request.DATA
        projectTitle = project_data.get("projectTitle")
        projectFramework = project_data.get("projectFramework")
        targetStream = project_data.get("targetStream")
        ieePaper = True if project_data.get("ieePaper") == "available" else False
        projectAbstract = project_data.get("projectAbstract")
        project_data_object = ProjectUploads(project_title=projectTitle, project_frame_work=projectFramework,
                                             target_stream=targetStream,
                                             iee_paper=ieePaper, abstract=projectAbstract, uploaded_user="srikanth")
        project_data_object.save()
        return Response({'result': 'success'}, 200)

    def delete(self, request):
        delete_data = request.DATA
        project_data = ProjectUploads.objects.get(id=delete_data.get("orderId"))
        project_data.isDeleted = True
        project_data.save()
        return Response({'result': 'success'}, 200)

    def put(self, request):
        update_form_data = request.DATA
        project_data = ProjectUploads.objects.get(id=update_form_data.get("projectId"))
        project_data.project_title = update_form_data.get("projectTitle")
        project_data.project_frame_work = update_form_data.get("projectFramework")
        project_data.target_stream = update_form_data.get("targetStream")
        project_data.iee_paper = True if update_form_data.get("ieePaper") == "available" else False
        project_data.abstract = update_form_data.get("projectAbstract")
        project_data.save()
        return Response({"result": "success"}, 200)

class BulkImportProjects(APIView):
    def post(self, request):
        input_excel = request.FILES['uploadFile']
        workbook = open_workbook(file_contents=input_excel.read())
        work_sheet = workbook.sheet_by_index(0)
        validation_report=ExcelValidations().validate_uploaded_sheet(work_sheet)
        if not validation_report:
            if request.user:
                uploaded_user = request.user.email
            else:
                uploaded_user = "annoyumus@pm.com"
            valid_projects_list = ExcelValidations().getValidatedProjectsList(work_sheet)
            save_projects_in_db(valid_projects_list, uploaded_user)
            print display_projects()
            return Response({"result":"success"}, 200)
        else:
            return Response({"result":"error","errorData":validation_report.get("result")}, 500)

def save_projects_in_db(projects_list, uploaded_user):
    for each_object in projects_list:
        project_id = datetime.utcnow().strftime("%y%m%d%H%M%S")
        project_title = each_object.get("PROJECT TITLE")
        project_frame_work = each_object.get("PROJECT FRAMEWORK")
        target_stream = each_object.get("PROJECT STREAM")
        iee_paper = [True if each_object["IEE PAPER"]=="YES" else False]
        abstract = each_object.get("PROJECT ABSTRACT")
        uploaded_user = uploaded_user
        project_provider = each_object.get("PROJECT PROVIDER ID")
        project_code = str(each_object.get("PROJECT ID", project_id))
        project_upload_object = ProjectUploads(project_id=project_id, project_title=project_title, project_frame_work=project_frame_work,
                       target_stream=target_stream, iee_paper=iee_paper, abstract=abstract, uploaded_user=uploaded_user,
                       project_provider=project_provider, project_code=project_code)
        project_upload_object.save()

def display_projects():
    projects_data = list()
    for each_project in ProjectUploads.objects.all():
         project_data = dict()
         project_data["project title"] = each_project.project_title
         project_data["project id"] = each_project.project_id
         project_data["provider"] = each_project.project_provider
         project_data["iee_paper"] = each_project.iee_paper
         project_data["project code"] = each_project.project_code
         projects_data.append(project_data)
    return projects_data


