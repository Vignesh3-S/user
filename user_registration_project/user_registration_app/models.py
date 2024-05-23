from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Registration(AbstractUser):
    Gender_choices = [("Select","Select"),("Male","Male"),("Female","Female"),("Others","Others")]
    Date_of_birth = models.DateField(verbose_name="Date of Birth",null=True,blank=True)
    Address = models.TextField(max_length=100,verbose_name="Address",null=True,blank=True)
    Mobile = PhoneNumberField(verbose_name="Mobile",help_text="give mobile number with country code (+xxx xxxxxxxxx)")
    gender = models.CharField(max_length=20,verbose_name="Gender",choices=Gender_choices)
    Userimg = models.ImageField(verbose_name='User Image', upload_to="userimages",null=True,blank=True)
    Updated_date = models.DateTimeField(auto_now=True,null=True,verbose_name="Updated Date")
    slug = models.SlugField(verbose_name="Slug Field",unique=True,max_length=30,null=True)
    
    def __str__(self):
        return self.username
    
    
