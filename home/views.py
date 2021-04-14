from django.shortcuts import render


def home(request):
    """ Returns the home page """
    template = 'home/home.html'
    context = {
        'title': 'home'
    }
    return render(request, template, context)


def about(request):
    """ Returns the about page """
    template = 'home/about.html'
    context = {
        'title': 'about'
    }
    return render(request, template, context)


def education(request):
    """ Returns the about page """
    template = 'home/education.html'
    context = {
        'title': 'education'
    }
    return render(request, template, context)


def experience(request):
    """ Returns the about page """
    template = 'home/experience.html'
    context = {
        'title': 'experience'
    }
    return render(request, template, context)


def contact(request):
    """ Returns the about page """
    template = 'home/contact.html'
    context = {
        'title': 'contact'
    }
    return render(request, template, context)
