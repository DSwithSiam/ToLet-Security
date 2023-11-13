from django.shortcuts import render, redirect
from users.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from tolet.settings import DEFAULT_FROM_EMAIL

UserModel = get_user_model()


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
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
            return redirect('dashboard')

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


@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html")


@login_required(login_url='login')
def editProfile(request):
    return render(request, "editProfile.html")


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

def admin_profile(request):
    return render(request, 'admin_profile.html')


def admin_edit_profile(request):
    return render(request, 'admin_edit_profile.html')
