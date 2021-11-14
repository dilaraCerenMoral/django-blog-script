from django.db import models

# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=200)
    last_edit_datetime = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    total_views = models.BigIntegerField(default=0,null=False, blank=True)
    image_name = models.CharField(max_length=100, null=True, blank=True)


class Comment(BaseModel):
    nickname = models.CharField(max_length=24)
    content = models.CharField(max_length=500)
    mail = models.CharField(max_length=320)




