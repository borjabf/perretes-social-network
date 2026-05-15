from django.shortcuts import render

# LoginView and LogoutView already created from core/urls.py
# View to render base.html
def index(request):
    return render(request, 'base.html')

