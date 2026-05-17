from django.shortcuts import render

# View to render the custom 404.html page
def custom_404(request, exception):
    return render(request, '404.html', status=404)
