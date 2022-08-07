from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NameForm(forms.Form):
    longitude = forms.FloatField()
    latitude = forms.FloatField()
    csrfmiddlewaretoken = forms.CharField()
    
class Utilisateur(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class Up(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']