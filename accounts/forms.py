from django import forms
from django.contrib.auth.forms import UserCreationForm
from lostdoc.models import User
from lostdoc.ugdistricts import DISTRICTS

#Create your forms here
class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=50, required=True, help_text="Required")
    lastname = forms.CharField(max_length=50, required=True, help_text="Required")
    email = forms.EmailField(max_length = 254, required = False, help_text="Required. Inform a valid email address")
    telephone_no = forms.IntegerField(required=True)
    address = forms.CharField(max_length=500, required=True)
    district = forms.CharField(max_length=50,  required=True)

    class Meta:
        model = User
        fields = ('username','firstname','lastname','email','telephone_no','address','district','password1','password2')