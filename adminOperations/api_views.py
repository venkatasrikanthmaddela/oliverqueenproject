from rest_framework.views import APIView

from rest_framework.response import Response


class UploadProjects(APIView):
    def post(self, request):
        return Response({'result':'success'}, 200)