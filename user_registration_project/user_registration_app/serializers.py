from rest_framework import serializers
from .models import Registration
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class Registration_Serializer(serializers.ModelSerializer):
    password = serializers.CharField( write_only=True,required=False,
        style={'input_type': 'password', 'placeholder': 'Password','minlength':8,'maxlength':15})
    confirm_password = serializers.CharField( write_only=True,required = False,
        style={'input_type': 'password', 'placeholder': 'Confirm Password','minlength':8,'maxlength':15})
    Date_of_birth = serializers.DateField( style={'placeholder': 'Date of birth'},required = True)
    Address = serializers.CharField(style={'input_type': 'textarea', 'placeholder': 'Full Address', 'maxlength':50},required=True)
    
    
    class Meta:
        model = Registration
        exclude = ['id','is_staff','is_active','is_superuser','date_joined','Updated_date','last_login','groups','user_permissions']
    
    def create(self,data): 
        try:
            validate_password(password=data.get('password'))
        except ValidationError as e:
            raise serializers.ValidationError(list(e))
        
        data.pop('confirm_password')    
        data['password'] = make_password(data.get('password'))
        data['slug'] = slugify(data.get('username'))
        data['is_active'] = True
        return super(Registration_Serializer,self).create(data)
    
    def update(self, instance,data):
        instance.slug = slugify(data.get('username',instance.username))
        return super(Registration_Serializer,self).update(instance,data)    
    