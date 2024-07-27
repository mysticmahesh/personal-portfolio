from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    message=models.TextField()
    def __str__(self):
        return self.name

class Projects(models.Model):
    title=models.CharField(max_length=60)
    description =models.TextField()
    image =models.ImageField(upload_to='projects',blank=True,null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title

