from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import ContactForm
from django.contrib import messages


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
    """ Returns the education page """
    template = 'home/education.html'
    context = {
        'title': 'education'
    }
    return render(request, template, context)


def experience(request):
    """ Returns the experience page """
    template = 'home/experience.html'
    context = {
        'title': 'experience'
    }
    return render(request, template, context)


def contact(request):
    """ Returns the contact page """
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['full_name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['matt.snell.00@hotmail.co.uk'])
            except BadHeaderError:
                HttpResponse('Bad Header Found')
            messages.success(request, 'Thanks for your message, \
                I will get back to you shortly')
            return redirect(reverse('contact'))
    template = 'home/contact.html'
    context = {
        'title': 'contact',
        'form': form,
    }
    return render(request, template, context)
