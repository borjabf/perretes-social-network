from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from barks.forms import BarkForm
from barks.models import Bark

# View to render the custom 404.html page
def custom_404(request, exception):
    return render(request, '404.html', status=404)


