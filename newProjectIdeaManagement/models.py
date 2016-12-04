from djangotoolbox.fields import DictField

from pmproject.models import CustomModel
from django.db import models
from userManagement.models import PmUser

class NewProjectIdea(CustomModel):
    customerId = models.ForeignKey('userManagement.PmUser')
    customerName = models.CharField(max_length=256)
    customerEmail = models.EmailField()
    customerMobile = models.CharField(max_length=256)
    projectTitle = models.TextField()
    projectStream = models.CharField(max_length=256)
    projectFramework = models.CharField(max_length=256)
    projectDescription = models.TextField()
    additionalData = DictField()
