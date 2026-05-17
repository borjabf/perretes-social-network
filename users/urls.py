from django.urls import path
from . import views

# Define paths from each url from each view
urlpatterns = [
    path('', views.signup, name='signup_home'), # home page is sign up page
    path ('signup/', views.signup, name='signup'), # signup url path
    path('profiles/<str:username>/', views.profile, name='profiles'), # profile.html url path (public and private)
    path('login-redirect/', views.login_redirect, name='login_redirect') # Intermediate route after logging in
]