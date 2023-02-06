from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    id = models.CharField(max_length = 32, primary_key = True)
    name = models.CharField(max_length = 64)
    description = models.TextField(null = True, max_length = 256)
    # members

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.CharField(max_length = 32, primary_key = True)
    content = models.TextField(max_length = 2048)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    # author = models.ForeignKey(User, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.content[0:32]