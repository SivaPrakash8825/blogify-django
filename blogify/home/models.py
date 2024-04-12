from django.db import models
class UserModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 
    
    
class UserPosts(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    post = models.CharField(max_length=255)  
    title = models.CharField(max_length=255)  