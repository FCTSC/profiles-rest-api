from django.contrib import admin

#importing custom model from profiles_api
from profiles_api import models


# Register your models here.

#Tells Django admin to register user profile model with admin site
# remain accessible through admin interface
admin.site.register(models.UserProfile)