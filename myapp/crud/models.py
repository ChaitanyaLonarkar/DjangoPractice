from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    age=models.IntegerField()
    


    def __str__(self):
        return self.name