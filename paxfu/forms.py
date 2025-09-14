from django.forms import ModelForm
from django import forms
from django.forms import TextInput, EmailInput
from django.contrib.auth.models import User
from .models import Person,Otp


class NameForm(forms.Form):
    class Meta:
        model=Person
        fields= ["email", "password",]

  
class otForm(forms.Form):
    class Meta:
        model=Otp
        fields= ["otp",]   