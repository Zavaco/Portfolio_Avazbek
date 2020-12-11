from django import forms
from django.forms import ModelForm
from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = FormCreate
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Your Name',
                    'id': 'name', 'required data-error': 'Please enter your name',
                    'name': 'name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Your E-mail',
                    'id': 'email', 'required data-error': 'Please enter your email',
                    'name': 'email'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Subject',
                    'id': 'msg_subject', 'required data-error': 'Please enter your Subject',

                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control', 'placeholder': 'Your Message',
                    'id': 'message', 'required data-error': 'Please enter your Message',
                }
            ),


        }
