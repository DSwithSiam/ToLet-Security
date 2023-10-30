from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-property/', views.add_property, name='addpost'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='log_out'),
    path('register/', views.user_signup, name='register'),
    path('about/', views.about, name='about'),
    path('sublet/', views.sublet, name='sublet'),
    path('setting/', views.setting, name='setting'),
    path('family/', views.family, name='family'),
    path('payment/', views.payment, name='payment'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path('office/', views.office, name='office'),
    path('services/', views.services, name='services'),
    path('saveproperty/', views.saveproperty, name='saveproperty'),
    path('wishlist/<int:pk>/', views.wishlist, name='wishlist'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editProfile, name='editProfile'),
    path('change_password/', views.changePassword, name='changePassword'),




]
