from dataclasses import field
from django import forms
from django.contrib.auth.models import User
#from localflavor.us.forms import USZipCodeField
# above is a packaged that6 is used for gwetting pincodes .
from .models import Profile
from .widgets import CustomPictureImageFieldWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    #bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio')