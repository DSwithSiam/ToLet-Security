from django.shortcuts import render, redirect
from users.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.mixins import UserPassesTestMixin

from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from tolet.settings import DEFAULT_FROM_EMAIL
from django.http import JsonResponse
from .models import *
UserModel = get_user_model()
from django.shortcuts import get_object_or_404


# Create your views here.
def get_districts(request, division_id):
    division = Division.objects.get(id=division_id)
    districts = District.objects.filter(division=division)
    data = [{'id': district.id, 'name': district.name} for district in districts]
    return JsonResponse(data, safe=False)

def get_upazilas(request, district_id):
    district = District.objects.get(id=district_id)
    upazilas = Upazila.objects.filter(district=district)
    data = [{'id': upazila.id, 'name': upazila.name} for upazila in upazilas]
    return JsonResponse(data, safe=False)


@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_superuser:
        sms = 'Page Not Found'
        return render(request, 'messages.html', {'sms': sms}) 
    else:
        return render(request, 'dashboard.html')


def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return redirect('dashboard')
                else:
                    # User authentication failed, so display an error message
                    messages.error(request, 'Invalid username or password')
            # If form is not valid, it will be re-rendered with form errors

        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('dashboard')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log in the user
            login(request, user)

            # Provide user feedback
            messages.success(
                request, 'You have successfully registered and logged in.')

            # Redirect to a dashboard or profile page
            # Change 'dashboard' to the name of your dashboard URL
            if not request.user.is_superuser:
                return render(request, "user_profile.html")
            else:
                return render(request, "dashboard.html")

        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('home')


def changePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})




def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = None

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = reverse('password_reset_confirm', args=(uid, token))
            current_site = get_current_site(request)
            mail_subject = 'Password Reset Request'
            message = render_to_string('reset_email.html', {
                'user': user,
                'domain': current_site.domain,
                'reset_link': reset_link,
            })

            send_mail(mail_subject, message, DEFAULT_FROM_EMAIL, [email])
        return render(request, 'password_reset_done.html', {'email': email})
    return render(request, 'password_reset_form.html')


def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            return redirect('password_reset_complete')
        return render(request, 'password_reset_confirm_form.html')
    else:
        return HttpResponse('Password reset link is invalid')


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')



@login_required(login_url='login')
def profile(request):
    # Assuming you have a one-to-one relationship between User and Profile models
    
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If the profile does not exist, create it
        profile = Profile.objects.create(user=request.user)
        
    
    if not request.user.is_superuser:
        return render(request, "user_profile.html", {'profile': profile})
    else:
        return render(request, "admin_profile.html", {'profile': profile})


@login_required(login_url='login')
def edit_profile(request):
    # Fetch all divisions, districts, and upazilas from the database
    divisions = Division.objects.all()
    districts = District.objects.all()
    upazilas = Upazila.objects.all()

    # Get the current user's profile
    profile = request.user.profile

    if request.method == 'POST':
        # Update User model fields
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        # Update Profile model fields
        profile.phone = request.POST.get('phone', '')

        # Fetch the Division instance based on the provided ID (assuming 'division' is the ID)
        division_id = request.POST.get('division', '')
        division = get_object_or_404(Division, id=division_id)
        profile.division = division

        # Fetch the District instance based on the provided ID (assuming 'district' is the ID)
        district_id = request.POST.get('district', '')
        district = get_object_or_404(District, id=district_id)
        profile.district = district

        # Fetch the Upazila instance based on the provided ID (assuming 'upazila' is the ID)
        upazila_id = request.POST.get('upazila', '')
        upazila = get_object_or_404(Upazila, id=upazila_id)
        profile.upazila = upazila

        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES.get('profile_picture')
            profile.save()


        profile.area = request.POST.get('area', '')
        profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')  # Redirect to the profile page after saving changes

    # Render the edit profile form with initial data
    context = {
        'divisions': divisions,
        'districts': districts,
        'upazilas': upazilas,
        'profile': profile,  # Include the user's profile in the context
    }

    if not request.user.is_superuser:
        return render(request, "editProfile.html", context)
    else:
        return render(request, 'admin_edit_profile.html', context)



