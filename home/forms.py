from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'message'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Full Name',
                                                'label': ''}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Email',
                                            'label': ''}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Message',
                                             'label': ''}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = ""
        self.fields['email'].label = ""
        self.fields['message'].label = ""
