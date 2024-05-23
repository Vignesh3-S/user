from django.shortcuts import render,redirect
from rest_framework import generics
from .serializers import Registration_Serializer
from .models import Registration
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib import messages

def home(request):
    return render(request,'user_registration_app/home.html')

class Get_All_Users(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_registration_app/showall.html'
    
    def get(self, request):
        queryset = Registration.objects.all()
        return Response({'users': queryset})

class Register_User(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = Registration_Serializer
    style = {'template_pack': 'rest_framework/vertical/'}
    template_name = 'user_registration_app/register_user.html'
    
    def get(self, request):
        return Response({'serializer': Registration_Serializer(),'style': self.style})

    def post(self, request):
        serializer = Registration_Serializer(data=request.data)
        try:
            pwd = len(request.data['password'])
            confirm_pwd = len(request.data['confirm_password'])
        except:
            messages.error(request,'Password and Confirm password should not be empty.')
            return redirect('createuser')
        if len(request.data['password']) < 8:
            messages.error(request,'password should be greater than 8 characters.')
            return redirect('createuser')
        if request.data['password'] != request.data['confirm_password']:
            messages.error(request,'password and confirm password must be same.')
            return redirect('createuser')
        if request.data['gender'] != 'Male' and request.data['gender'] != 'Female' and request.data['gender'] != 'Others':
            messages.error(request,'Select any gender.')
            return redirect('createuser')
        
        if not serializer.is_valid():
            messages.error(request,serializer.errors)
            return redirect('createuser')
        serializer.save()
        messages.success(request,'Registered Successfully')
        return redirect('allusers')
        
class Get_User(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = Registration_Serializer
    style = {'template_pack': 'rest_framework/vertical/'}
    template_name = 'user_registration_app/getuser.html'
    lookup_field = 'slug'
    
    def get(self, request,slug):
        queryset = Registration.objects.get(slug=slug)
        return Response({'users': queryset})

class Update_User(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = Registration_Serializer
    style = {'template_pack': 'rest_framework/vertical/'}
    lookup_field = 'slug'
    template_name = 'user_registration_app/update.html'
    
    def get(self, request, slug):
        profile = get_object_or_404(Registration, slug=slug)
        serializer = Registration_Serializer(profile)
        return Response({'serializer': serializer, 'profile': profile,'style': self.style})

    def post(self, request, slug):
        profile = get_object_or_404(Registration, slug=slug)
        serializer = Registration_Serializer(profile, data=request.data)
        if not serializer.is_valid():
            messages.error(request,serializer.errors)
            return redirect('updateuser',slug=profile.slug)
        serializer.save()
        messages.success(request,'Updated Successfully')
        return redirect('getuser',slug=profile.slug)

class Delete_User(APIView):
    def get(self,request,slug):
        profile = Registration.objects.get(slug=slug)
        try:
            profile.Userimg.delete()
        except:
            messages.error(request,'Contact admin')
        profile.delete()
        messages.success(request,'Deleted Successfully')
        return redirect('allusers')
        