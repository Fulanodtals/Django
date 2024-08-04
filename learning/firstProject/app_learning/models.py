from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)#numera os usuarios crecente
    name = models.TextField(max_length='255')
    age = models.IntegerField()