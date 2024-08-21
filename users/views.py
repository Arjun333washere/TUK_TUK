#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages

from django.utils.decorators import method_decorator #used for class basedv viwws
from .forms import * #used to view profile forms
from auto.models import Listing,LikedListing
# Create your views here.



def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(
                    request,f'you are loggrrfd in as {username}')
                return redirect('home')
        else:
            messages.error(request,f'this shows it failed loggin in ')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form})

#@login_required
def index_view(request):
    return render(request,"views/index.html")




class RegisterView(View):
    def get(self,request):
        register_form = UserCreationForm()
        return render(request,"views/register.html",{'register_form':register_form})

    def post(self,request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request,user)
            return redirect('home')
        else:
            print("eroor while registering")
            return render(request, 'views/register.html', {'register_form': register_form})
            #messages.error(request,f'An error occured trying to register')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



@method_decorator(login_required,name='dispatch')
class ProfileView(View):

    def get(self,request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(
            profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request,'views/profile.html',{'user_form': user_form,'profile_form': profile_form,'user_listings': user_listings,'user_liked_listings': user_liked_listings})
    
    def post(self,request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(
            profile=request.user.profile).all()
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile saved successfully')
        else :
            messages.error(request,"eroor occourde while saving")

        return render(request,'views/profile.html',{'user_form': user_form,'profile_form': profile_form,'user_listings': user_listings,'user_liked_listings': user_liked_listings})
                                                      
    







""" def register_view(request):
    register_form = UserCreationForm()
    return render(request,"views/register.html",{'register_form':register_form})

def registerPost_view(request):
    register_form = UserCreationForm(data=request.POST)
    if register_form.is_valid():
        user = register_form.save()
        user.refresh_from_db()
        login(request,user)
        return redirect('home')
    else:
        print("eroor in registgering")
        return render(request,"views/register.html",{'register_form':register_form}) """


