from django import forms
from django.forms.models import inlineformset_factory
from .models import Course,Module

ModuleFormSet		=		inlineformset_factory(Course,Module,fields=['title','description'],extra=2,can_delete=True)


class ContactForm(forms.Form):
    contact_name=forms.CharField(label='Enter your Name', required=True)
    contact_email=forms.EmailField(label='Enter your Email', required=True)
    contact_no = forms.CharField(label='Enter your contact phone number')
    content=forms.CharField(label='Enter your message',required=True,widget=forms.Textarea)