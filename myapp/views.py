from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User



# Create your views here.


def home(request):
    return render(request, 'index.html')


def add_property(request):
    if not request.user.is_authenticated:
        # if user not authenticate, then exicute this code
        return redirect('login')
    else:
        return render(request, 'addproperty.html')


def about(request):
    return render(request, 'about.html')


def sublet(request):
    return render(request, 'sublet.html')


def setting(request):
    return render(request, 'setting.html')


def family(request):
    return render(request, 'family.html')


def payment(request):
    return render(request, 'payment.html')


def bachelor(request):
    return render(request, 'bachelor.html')


def office(request):
    return render(request, 'office.html')


def services(request):
    services = Service.objects.all()[:2]
    return render(request, 'services.html', {'services': services})


# @login_required(login_url='')
def saveproperty(request):
    # wishlists = wishlist.object.filter(user=request.user)
    # return render(request, 'saveproperty.html', {'wishlists': wishlists})
    if not request.user.is_authenticated:
        # if user not authenticate, then exicute this code
        return redirect('login')
    else:
        return render(request, 'saveproperty.html')


def user_dashboard(request):
    return render(request, 'dashboard.html')


def wishlist(request, pk):
    property = property.objects.get(id=pk)
    wishlist.object.create(property=property, user=request.user)
    return render(request, 'wishlist.html')

# User Log in


def log_in(request):
    if not request.user.is_authenticated:
        # if user not authenticate, then exicute this code
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                # check validation so we need cleaned data
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return redirect('dashboard')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('dashboard')
# User sign UP


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulation! you have created an account successfully!!')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('home')

def changePassword(request):
    form = ChangePasswordForm(user=request.user)
    
    return render(request, 'changePassword.html',{'form':form})
                  
def profile (request):
    user = UserData()
    print(user)
    return render (request, "profile.html" , { "member":user})

def editProfile (request):
    return render (request, "editProfile.html")