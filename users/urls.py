from django.urls import path
from . import views

# Define paths from each url from each view
urlpatterns = [
    path('signup/', views.signup, name='signup'), # signup.html url path
    path('my-profile/', views.profile, name='my-profile'), # profile.html url path
]