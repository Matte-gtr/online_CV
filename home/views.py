from django.shortcuts import render


def home(request):
    """ Returns the home page """
    template = 'home/home.html'
    return render(request, template)
