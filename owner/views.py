from django.shortcuts import render, get_object_or_404,\
    reverse, redirect
from django.contrib.auth.decorators import login_required

from home.models import Contact


@login_required
def profile(request):
    """ a view for the owners profile """
    messages = Contact.objects.all().order_by('-date_recieved')
    template = 'owner/profile.html'
    context = {
        'title': 'profile',
        'messages': messages,
    }
    return render(request, template, context)


@login_required
def read_message(request, contact_id):
    """ a view to read a message """
    message = get_object_or_404(Contact, pk=contact_id)
    message.unread = False
    message.save(update_fields=['unread'])
    template = 'owner/message.html'
    context = {
        'title': 'message',
        'message': message,
    }
    return render(request, template, context)


@login_required
def delete_message(request, contact_id):
    """ a view to delete a message """
    message = get_object_or_404(Contact, pk=contact_id)
    message.delete()
    return redirect(reverse('profile'))


@login_required
def mark_unread(request, contact_id):
    message = get_object_or_404(Contact, pk=contact_id)
    message.unread = True
    message.save(update_fields=['unread'])
    return redirect(reverse('profile'))
