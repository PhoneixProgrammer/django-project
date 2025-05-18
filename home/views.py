from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# This is a view function that renders the home page.
# It uses the render function to combine a template with a context and return an HttpResponse object.
def home(request):
    return render(request, "home/index.html")
def success_page(request):
    return HttpResponse("<h1>Success! You're at the success page.</h1>")