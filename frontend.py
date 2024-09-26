# user_model

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    mobile = models.CharField(max_length=128, blank=False, null=False)
    email = models.CharField(max_length=128, blank=False, null=False)
    last_login = models.DateTimeField(blank=False, null=False)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_user(self, name, mobile, email):
        # Function to create a new user in the database
        pass

    def fetch_user(self, user_id):
        # Function to fetch user information from the database
        pass

    def update_user(self, user_id, data):
        # Function to update user information in the database
        pass

# role_model.py

class Role(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    slug = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# resource_model.py

class Resource(models.Model):
    slug = models.CharField(max_length=256, blank=False, null=False)
    name = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
