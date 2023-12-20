
from django.shortcuts import render

def index(request):
    """Home page, index view"""

    return render(request, "index.html")
