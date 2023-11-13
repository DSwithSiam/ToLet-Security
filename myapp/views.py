from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Add_property

# Create your views here.


def home(request):
    home = Add_property.objects.all()
    # return render(request, 'chocolate/services.html', {'services': services})
    return render(request, 'index.html', {'home': home})


@login_required(login_url='login')
def add_property(request):
    if request.method == "POST":
        propertytype = request.POST.get('propertytype')
        division = request.POST.get('division')
        district = request.POST.get('district')
        areaname = request.POST.get('areaname')
        images = request.POST.get('images')

        addproperty = Add_property(propertytype=propertytype, division=division,
                                   district=district, areaname=areaname, images=images)
        addproperty.save()
    return render(request, 'addproperty.html')


def about(request):
    return render(request, 'about.html')


def sublet(request):
    return render(request, 'sublet.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'settings.html')


def family(request):
    return render(request, 'family.html')


@login_required(login_url='login')
def payment(request):
    return render(request, 'payment.html')


def bachelor(request):
    return render(request, 'bachelor.html')


def office(request):
    return render(request, 'office.html')


def services(request):
    services = Service.objects.all()[:2]
    return render(request, 'services.html', {'services': services})


@login_required(login_url='login')
def saveproperty(request):
    # wishlists = wishlist.object.filter(user=request.user)
    # return render(request, 'saveproperty.html', {'wishlists': wishlists})
    if not request.user.is_authenticated:
        # if user not authenticate, then exicute this code
        return redirect('login')
    else:
        return render(request, 'saveproperty.html')


@login_required(login_url='login')
def wishlist(request, pk):
    property = property.objects.get(id=pk)
    wishlist.object.create(property=property, user=request.user)
    return render(request, 'wishlist.html')

def contact(request):
    return render(request, 'contact.html')

def property_single(request):
    return render(request, 'property_single.html')

def terms_condition(request):
    return render(request, 'terms_condition.html')

def faq(request):
    return render(request, 'faq.html')