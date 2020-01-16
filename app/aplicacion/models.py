from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=200, null = False)
    password = models.CharField( max_length=200, null = False)
    correo = models.CharField( max_length=200, null = False)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    consult = models.CharField(max_length=1000)

class Commentary(models.Model):
    id = models.AutoField(primary_key = True)
    postid = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
