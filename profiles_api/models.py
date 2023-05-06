from django.db import models
# These are standard base classes neede when overiding/customizing default Django
# Django user Model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        # For password argument-> if you dont specify, it will default to None
        # However Django's password checking system doesnt not allow a no password

        """ Create a new user"""

        #IF email is passed either a empty string or null value
        # Raise a value error exception and display error message to user
        if not email:
            raise ValueError('User must have an email address')
        
        #Normailizing email addres -> makes 2nd half of email address all lowercase
        email = self.normalize_email(email)
        # Create user model and set email and name
        user = self.model(email=email,name=name)

        #Password is encrypted -> converted to hash and not stored as plaintext
        user.set_password(password)

        #Save user model
        #using = self._db -> save to db(Best practise to add this to support multiple databases)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """Create and save new superuser with given details"""
        #self is auto passed in for any class functions that is called
        # That's why no need to pass self
        user = self.create_user(email,name,password)

        # Don't need to specify is_superuser. It is auto created  by the PermissionsMixin
        user.is_superuser = True
        user.is_staff= True
        user.save(using=self._db)

        return user






class UserProfile (AbstractBaseUser, PermissionsMixin):
    # Describes what the class does
    """Database model for users in  the system"""
    
    # We want a email column in our UserProfile DB. Email to have max
    #length of 255 char and emails are unique. Cant have 2 same email in DB
    email = models.EmailField(max_length=255, unique= True)

    name = models.CharField(max_length=255)

    #Determine if user's profile is activated (Only True or False value)
    is_active = models.BooleanField(default=True)
    #Determine if user should have access to Django admin and others privlleges
    is_staff = models.BooleanField(default= False)

    # NEED TO SPECIFY model manager
    # Django needs to have a custom model manageer to know
    # how to create and control users using Django CLI

    objects = UserProfileManager()

    #Need to specifiy username as we are overiding default username field
    #Needed to work with Django admin and authentication system

    # When authenticating users -> will be asking for email address and password
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    #Because we are defining function in a class -> need to specify self
    # as the first argument
    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name
    
    # Converting the user object into a string in python
    def __str__(self):
        """ Return string representation of user"""
        return self.email
