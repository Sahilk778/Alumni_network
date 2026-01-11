from django.db import models
from django.contrib.auth.models import User

class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduation_year = models.IntegerField()
    department = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
