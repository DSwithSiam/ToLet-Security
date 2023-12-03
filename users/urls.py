from django.urls import path
from users import views


# create urls here
urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.signin, name='login'),
    path('logout/', views.log_out, name='log_out'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.changePassword, name='change-password'),
    path('profile/', views.profile, name='profile'),
    
    # path('password-reset/', views.password_reset, name='password-reset'),
    # path('password-reset-done/', views.password_reset_done, name='password-reset-done'),
    # path('password-reset-confirm/', views.password_reset_confirm, name='password-reset-confirm'),



    # reset password url
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-done/', views.password_reset_done,
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete,
         name='password_reset_complete'),


     path('get_districts/<int:division_id>/', views.get_districts, name='get_districts'),
     path('get_upazilas/<int:district_id>/', views.get_upazilas, name='get_upazilas'),
]
