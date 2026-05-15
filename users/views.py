from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# View to register new user
def signup(request):
    # if user sends form to signup
    if request.method == 'POST':
        # Filling form data sent by the user
        form = UserCreationForm(request.POST)
        if form.is_valid(): # Checks if username and email are valid
            user = form.save() # Persists the new user in the DB and save return in "user"
            login(request, user) # Login of the new user created
            return redirect('profile') # Redirect to the profile template
    # If method is GET
    else:
        form = UserCreationForm() # Sends empty form
    # Whether method is GET or some error raised, shows the form template
    return render(request, 'users/signup.html', {'form': form})

# Temporal view
def profile(request):
    return render(request, 'users/profile.html')