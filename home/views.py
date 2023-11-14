from django.shortcuts import render

def home(request):
    """This view renders the homepage, including product displays"""
    return render(request, 'home/index.html')
