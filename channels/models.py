from django.db import models


# Create your models here.
class Tags(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.tag_name

class Channel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=100)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=100)
    usr = models.IntegerField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    postedOn = models.DateTimeField(auto_now_add=True)