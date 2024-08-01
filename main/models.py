from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.TextField()
    date = models.DateField()

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.task}] --- created at --> [{self.date}]"

    

class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile_pic/")

    def __str__(self):
        return self.title




 
    
    