from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [
        ("present", "Present"),
        ("absent", "Absent"),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField(auto_now_add=True)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices= STATUS_CHOICES,
        default="present"
    )

    def __str__(self):
        return f"{self.employee.username} - {self.date} - {self.status}"
