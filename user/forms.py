from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

REGION = (
    ('','Select'),
    ('NE','Northern Europe'),
    ('SCA','South-Central Asia'),
    ('SE','Southern Europe'),
    ('WA','West Africa'),
    ('ME','Middle East'),
)

class SignupForm(UserCreationForm):
    region = forms.ChoiceField(choices=REGION)
    class Meta:
        model = User
        fields = ['username','email', 'region','password1', 'password2']
