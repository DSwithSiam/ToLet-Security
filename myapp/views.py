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
        # property Information
        status = request.POST.get('status')
        propertytype = request.POST.get('propertytype')
        size = request.POST.get('size')
        bedroom = request.POST.get('bedroom')
        drawingroom = request.POST.get('drawingroom')
        diningroom = request.POST.get('diningroom')
        balcony = request.POST.get('balcony')
        washroom = request.POST.get('washroom')
        rules = request.POST.get('rules')
        comment = request.POST.get('comment')

        # Add Location
        division = request.POST.get('division')
        district = request.POST.get('district')
        areaname = request.POST.get('areaname')

        # Facilities
        lift = request.POST.get('lift')
        gas = request.POST.get('gas')
        garage = request.POST.get('garage')
        cc_camera = request.POST.get('cc_camera')
        security_guard = request.POST.get('security_guard')
        swiming_pool = request.POST.get('swiming_pool')
        store_room = request.POST.get('store_room')
        fire_extinguisher = request.POST.get('fire_extinguisher')

        # Add Images
        images = request.POST.get('images')

        # Owner Information
        owner_name = request.POST.get('owner_name')
        contact_number = request.POST.get('contact_number')
        whatsapp_number = request.POST.get('whatsapp_number')

        addproperty = Add_property(propertytype=propertytype, division=division,
                                   district=district, areaname=areaname, images=images)
        addproperty.save()
    return render(request, 'addproperty.html')


def about(request):
    return render(request, 'about.html')


def tutorial(request):
    return render(request, 'tutorial.html')


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contact with us.')
            return redirect('home')  # Redirect to a success page

        else:
            messages.error(request, "Invalid form data.")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def property_single(request):
    return render(request, 'property_single.html')


def privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.first()
    return render(request, 'privacy_policy.html', {'privacy_policy': privacy_policy})


def terms_and_conditions(request):
    terms_and_conditions = TermsAndConditions.objects.first()
    return render(request, 'terms_conditions.html', {'terms_and_conditions': terms_and_conditions})


def faqs(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def Emergency(request):
    return render(request, 'Emergency.html')

# @login_required(login_url='login')
# def add_property_two(request):
#     if request.method == "POST":
#         # property Information
#         status = request.POST.get('status')
#         propertytype = request.POST.get('propertytype')
#         size = request.POST.get('size')
#         bedroom = request.POST.get('bedroom')
#         drawingroom = request.POST.get('drawingroom')
#         diningroom = request.POST.get('diningroom')
#         balcony = request.POST.get('balcony')
#         washroom = request.POST.get('washroom')
#         rules = request.POST.get('rules')
#         comment = request.POST.get('comment')

#         # Add Location
#         division = request.POST.get('division')
#         district = request.POST.get('district')
#         areaname = request.POST.get('areaname')

#         # Facilities
#         lift = request.POST.get('lift')
#         gas = request.POST.get('gas')
#         garage = request.POST.get('garage')
#         cc_camera = request.POST.get('cc_camera')
#         security_guard = request.POST.get('security_guard')
#         swiming_pool = request.POST.get('swiming_pool')
#         store_room = request.POST.get('store_room')
#         fire_extinguisher = request.POST.get('fire_extinguisher')

#         # Add Images
#         images = request.POST.get('images')

#         # Owner Information
#         owner_name = request.POST.get('owner_name')
#         contact_number = request.POST.get('contact_number')
#         whatsapp_number = request.POST.get('whatsapp_number')

#         addproperty = Add_property(propertytype=propertytype, division=division,
#                                    district=district, areaname=areaname, images=images)
#         addproperty.save()
#     return render(request, 'addproperty.html')
