from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    photoURL = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    country = models.JSONField(blank=True, null=True)  # Use JSONField for JSON data
    state = models.JSONField(blank=True, null=True)
    city = models.JSONField(blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else self.user_id
