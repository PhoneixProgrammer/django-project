from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# This is a view function that renders the home page.
# It uses the render function to combine a template with a context and return an HttpResponse object.
def home(request):
    peoples = [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Doe", "age": 22},
    ]
    text ="""Hello, this is a simple text that will be passed to the template."""
    vegetables=["carrot","potato","onion"]

 

    return render(request, "home/index.html",context={"peoples": peoples,"text": text,"vegetables": vegetables,"page":"Home Page"})
    #with the help of context we are sending backend data to html  template

def about(request):
    return render(request, "home/about.html", context={"page": "About Us"})
def contact(request):
    return render(request, "home/contact.html", context={"page": "Contact Us"})
def success_page(request):
    return HttpResponse("<h1>Success! You're at the success page.</h1>")