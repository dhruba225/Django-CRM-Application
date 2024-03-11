from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
  email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
  first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
  last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
  username = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
  password1 = forms.CharField(label="",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
  password2 = forms.CharField(label="",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','password1','password2']


class AddRecordForm(forms.ModelForm):
  first_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
  last_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
  email = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
  phone = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
  address = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
  city = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
  state = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}))
  zipcode = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}))

  class Meta:
    model = Record
    exclude = ('user',)
