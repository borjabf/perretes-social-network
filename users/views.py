from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from barks.forms import BarkForm
from barks.models import Bark

# LoginView and LogoutView already created from core/urls.py (Django native)

# View to register new user
def signup(request):
    # If the user is logged in and goes to home or tries to log in again, they are redirected to their profile
    if request.user.is_authenticated:
        return redirect('profiles', username=request.user.username)
    # if user sends form to signup
    if request.method == 'POST':
        # Filling form data sent by the user
        form = UserCreationForm(request.POST)
        if form.is_valid(): # Checks if username and email are valid
            user = form.save() # Persists the new user in the DB and save return in "user"
            login(request, user) # Login of the new user created
            return redirect('profiles', username=user.username) # Redirect to the profile template
    # If method is GET
    else:
        form = UserCreationForm() # Sends empty form
    # Whether method is GET or some error raised, shows the form template
    return render(request, 'users/signup.html', {'form': form})


# View to render public and private profiles
@login_required # Decorator to require log in to watch public or private profiles
def profile(request, username):
    # Find username in db with get_object_or_404
    user_profile = get_object_or_404(User, username=username)

    # Check if user with that username is the one who logged in, and if is the one with the same username searched
    is_own_profile = request.user.is_authenticated and request.user == user_profile

    # Instantiation of the form variable to prevent the code from breaking
    form = None

    # ONLY IF USER IS VISITING THEIR OWN PROFILE (PRIVATE)
    # POST: manage bark form
    if is_own_profile: # Checks if the users is the owner of the profile
        if request.method == 'POST':  # Checks the method of the request
            form = BarkForm(request.POST)  # Pass the request data to the BarkForm form
            if form.is_valid():  # If form validation is correct
                bark = form.save(commit=False)  # Commits (not save in DB yet) the 'content' of the bark
                # this prevents errors by saving the record to the database without the required field (username)
                bark.user = request.user  # adds to the bark object the username logged in
                bark.save()  # Saves bark object in DB with all required data
                return redirect('profiles', username=username)  # Redirect to the same page

        # GET: render profile page and show history barks (public profiles)
        else:  # If method is not POST (so GET) or !form.is_valid()
            form = BarkForm()  # Renders an empty BarkForm form

    user_barks = Bark.objects.filter(user=request.user).order_by('-created_at')  # Sends a query to the DB
    # that retrieves all records from table Bark from the user who is logged in

    context = {
        'form': form,
        'user_barks': user_barks,
        'user_profile': user_profile,
        'is_own_profile': is_own_profile
    }  # Creates variables to serve as a context
    # for the variables contained in the form and the data from this view,
    # in order to pass them to the template

    return render(request, 'users/profile.html', context)  # Renders this view into template 'profile'

# Intermediate view to pass the username to the destination URL after login (in setting.py)
@login_required
def login_redirect(request):
    return redirect('profiles', username=request.user.username)