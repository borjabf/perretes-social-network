from django.urls import path
from . import views

# Define paths from each url from each view
urlpatterns = [
    path('profile/<str:username>/', views.wall, name='wall')
]