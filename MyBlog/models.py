from django.db import models

class newPost(models.Model):
    tituloPost = models.TextField(max_length = 100)
    post = models.TextField(max_length = 10000)

# Create your models here.
