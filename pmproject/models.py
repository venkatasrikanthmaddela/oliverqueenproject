from django.db import models

from datetime import datetime
from django_mongodb_engine.contrib import MongoDBManager


class CustomManager(MongoDBManager):
    def get_query_set(self):
        return super(CustomManager, self).get_query_set().filter(isDeleted=False)

class CustomModel(models.Model):
    createdAt = models.DateTimeField(default=datetime.utcnow())
    modifiedAt = models.DateTimeField(default=datetime.utcnow())
    isDeleted = models.BooleanField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or not self.createdAt:
            self.createdAt = datetime.utcnow()
        self.modifiedAt = datetime.utcnow()
        super(CustomModel, self).save(*args, **kwargs)

    def delete(self):
        self.isDeleted = True
        super(CustomModel, self).save()

    def hardDelete(self):
        super(CustomModel, self).delete(self)