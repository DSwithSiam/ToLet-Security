from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-property/', views.add_property, name='addpost'),
    path('about/', views.about, name='about'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('sublet/', views.sublet, name='sublet'),
    path('settings/', views.settings, name='settings'),
    path('family/', views.family, name='family'),
    path('payment/', views.payment, name='payment'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path('office/', views.office, name='office'),
    path('services/', views.services, name='services'),
    path('saveproperty/', views.saveproperty, name='saveproperty'),
    path('wishlist/<int:pk>/', views.wishlist, name='wishlist'),
    path('contact/', views.contact, name='contact'),
    path('property-single/', views.property_single, name='property-single'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('faqs/', views.faqs, name='faqs'),
    path('Emergency/', views.Emergency, name='Emergency'),

]
