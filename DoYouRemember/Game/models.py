from django.db import models

# Create your models here.
class UserInput(models.Model):
    user_text = models.TextField(max_length='255')
    new_text  = models.TextField(max_length='255')