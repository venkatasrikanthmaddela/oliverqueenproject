from django.db import models

from pmproject.models import CustomModel


class ProjectUploads(CustomModel):
    project_id = models.TextField(max_length=256)
    project_title = models.CharField(max_length=256)
    project_frame_work = models.CharField(max_length=256)
    target_stream = models.CharField(max_length=256)
    iee_paper = models.BooleanField(default=True)
    abstract = models.TextField()
    uploaded_user = models.EmailField()
    project_provider = models.TextField(max_length=200)
    project_code = models.TextField(max_length=256)
