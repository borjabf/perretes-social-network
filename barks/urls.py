from django.urls import path
from . import views

# Define paths from each url from each view
urlpatterns = [
    path('profile/<str:username>/', views.wall, name='wall'),
# # Temporary route for 404.html page to style it
#     path('test-404/', views.custom_404, {'exception': Exception()})
]