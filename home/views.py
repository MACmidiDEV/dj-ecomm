from django.shortcuts import render

# Create your views here.
def index(request):
    """Display landing page"""
    return render(request, "index.html")