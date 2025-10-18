from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Portfolio(models.Model):
    # Basic info
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    resume = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Education
    age = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=200, blank=True, null=True)
    graduation_year = models.CharField(max_length=10, blank=True, null=True)

    # Experience
    company = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)

    # Projects
    projects_title = models.CharField(max_length=200, blank=True, null=True)
    project_desc = models.TextField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)

    # Skills
    skills = models.TextField(blank=True, null=True)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username