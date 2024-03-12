from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Project(models.Model):
    name = models.CharField(max_length=255)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    tasks = models.CharField(
        max_length=500, 
        blank=True,
        null=True,
        default=["Task1", "Task2", "Task3"]
        )

    def __str__(self):
        return self.name

class TimeEntry(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    task_name = models.CharField(max_length=255)
    start_timestamp = models.DateTimeField(null=True)
    end_timestamp = models.DateTimeField(null=True)
    current_duration = models.DecimalField(null=True, decimal_places=2, max_digits=3)

    def __str__(self):
        return f"{self.project_name} - {self.task_name}"
