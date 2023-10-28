from django.shortcuts import redirect, render
from myapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'index.html')

def add_property(request):
    return render(request,'addproperty.html')

def log_in(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        fullName = request.POST.get("fullName")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        rg_user = User.objects.create_user(fullName, phone, email, password)
        # rg_user = Register(name = fullName, phone = phone, email = email, password = password)
        
        rg_user.save()
        print(fullName, phone, email, password)
        return redirect("login.html")
    
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def sublet(request):
    return render(request,'sublet.html')

def setting(request):
    return render(request,'setting.html')

def family(request):
    return render(request,'family.html')

def payment(request):
    return render(request,'payment.html')

def bachelor(request):
    return render(request,'bachelor.html')

def office(request):
    return render(request,'office.html')

def services(request):
    services = Service.objects.all()[:2]
    return render(request,'services.html', {'services': services})

@login_required(login_url='')
def saveproperty(request):
    wishlists = wishlist.object.filter(user=request.user)
    return render(request,'saveproperty.html', {'wishlists': wishlists})

def profile(request):
    return render(request,'profile.html')

def editProfile(request):
    return render(request,'editProfile.html')

def signup(request):
    return render(request,'signup.html')

def wishlist(request, pk):
    property = property.objects.get(id=pk)
    wishlist.object.create(property=property, user=request.user)
    return render(request,'wishlist.html')


