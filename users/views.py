from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from barks.forms import BarkForm
from barks.models import Bark


# View to register new user
def signup(request):
    # if user sends form to signup
    if request.method == 'POST':
        # Filling form data sent by the user
        form = UserCreationForm(request.POST)
        if form.is_valid(): # Checks if username and email are valid
            user = form.save() # Persists the new user in the DB and save return in "user"
            login(request, user) # Login of the new user created
            return redirect('my-profile') # Redirect to the profile template
    # If method is GET
    else:
        form = UserCreationForm() # Sends empty form
    # Whether method is GET or some error raised, shows the form template
    return render(request, 'users/signup.html', {'form': form})

# View that displays a user's bark using the GET method,
# and handles the barking form using the POST method
@login_required # Decorator to require log in for the user
def profile(request):
    # POST: manage bark form
    if request.method == 'POST': # Checks the method of the request
        form = BarkForm(request.POST) # Pass the request data to the BarkForm form
        if form.is_valid(): # If form validation is correct
            bark = form.save(commit=False)  # Commits (not save in DB yet) the 'content' of the bark
            # this prevents errors by saving the record to the database without the required field (username)
            bark.user = request.user # adds to the bark object the username logged in
            bark.save() # Saves bark object in DB with all required data
            return redirect('my-profile') # Redirect to the same page

    # GET: render profile page and show history barks
    else: # If method is not POST (so GET) or !form.is_valid()
        form = BarkForm() # Renders an empty BarkForm form

    user_barks = Bark.objects.filter(user=request.user).order_by('-created_at') # Sends a query to the DB
    # that retrieves all records from table Bark from the user who is logged in

    context = {'form': form, 'barks': user_barks} # Creates variables to serve as a context
    # for the variables contained in the form and the data from this view,
    # in order to pass them to the template

    return render(request, 'users/profile.html', context) # Renders this view into template 'profile'
