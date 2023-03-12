from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    name = models.CharField(max_length=100)
    assigned = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, default=None,blank=True)
    approved_time = models.DateTimeField(null=True, default=None,blank=True)
    approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='task_images',null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']

