from django.urls import path
from . import views

# Define paths from each url from each view
urlpatterns = [
    path('', views.index, name='index'), # base.html url path
]