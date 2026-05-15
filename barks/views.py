from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from barks.models import Bark


# LoginView and LogoutView already created from core/urls.py (Django native)

def wall(request, username):
    # Find username in db with get_object_or_404
    user_profile = get_object_or_404(User, username=username)

    # Get all barks from the user (user_profile object)
    user_barks = Bark.objects.filter(user=user_profile).order_by('-created_at')

    # Context to implement in Template
    context = {'user_barks': user_barks, 'user_profile': user_profile}

    # Render template wall.html with the context
    return render(request, 'barks/wall.html', context)


