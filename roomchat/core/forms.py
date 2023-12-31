from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    BLOOD_TYPE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    RH_FACTOR_CHOICES = [
        ('+', 'Positive'),
        ('-', 'Negative'),
    ]

    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES, required=True, help_text='Required. Select your blood type.')
    rh_factor = forms.ChoiceField(choices=RH_FACTOR_CHOICES, required=True, help_text='Required. Select your Rh factor.')


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','blood_type','rh_factor','email','password1', 'password2']