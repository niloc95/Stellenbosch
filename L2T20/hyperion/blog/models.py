from django.db import models

# Create your models here.
class Post(models.Model):
# Default behaviour - Django creates primary keys for you
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Nilo here, this django II")
    date = models.DateTimeField()

def __str__(self):
    return self.title