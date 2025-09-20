from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    ROLE_CHOICES = [
        ('employee', "Employee"),
        ('manager', "Manager"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") 
    role = models.CharField(max_length=100, choices= ROLE_CHOICES, default="employee")
    department = models.CharField(max_length=100, blank=True, null=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

