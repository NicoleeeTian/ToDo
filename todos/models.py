from django.db import models

# Create your models here.


# Database schema
class Task(models.Model):
    task = models.CharField(max_length = 250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # string representation
        return self.task