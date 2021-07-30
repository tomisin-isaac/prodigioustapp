from django import forms 
from django.forms import ModelForm
from django.forms import TextInput,EmailInput,FileInput,Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField
from django.forms.widgets import Select

from.models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,help_text='username')
    first_name = forms.CharField(max_length=50,help_text='first_name')
    last_name = forms.CharField(max_length=50,help_text='last_name')
    email = forms.EmailField(max_length=50,help_text='email')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


    def save(self,commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



STATE = [
    ('Abia','Abia'),
    ('Akwa-ibom','Akwa-ibom'),
    ('Edo','Edo'),
    ('Imo','Imo'),
    ('Lagos','Lagos'),
    ('Ogun','Ogun'),
    ('Ondo','Ondo'),
    ('Oyo','Oyo'),
    ('Rivers','Rivers'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','phone','address','city','state','country','images')
        widgets = {
            'first_name': TextInput(attrs={'class':'input','placeholder':'First Name'}),
            'last_name': TextInput(attrs={'class':'input','placeholder':'last Name'}),
            'email': EmailInput(attrs={'class':'input','placeholder':'Email'}),
            'phome': TextInput(attrs={'class':'input','placeholder':'phone'}),
            'address': TextInput(attrs={'class':'input','placeholder':'Address'}),
            'city': TextInput(attrs={'class':'input','placeholder':'City'}),
            'state': Select(attrs={'class':'select','placeholder':'State'},choices=STATE),
            'country':TextInput(attrs={'class':'input','placeholder':'Country'}),
            'images':FileInput(attrs={'placeholder':'images'}),
        }