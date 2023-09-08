from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from shop.bulma_mixin import BulmaMixin

class SignUpForm(BulmaMixin, UserCreationForm):
    first_name = forms.CharField(label='Write ypur first name')
    last_name = forms.CharField(label='Write your last name')
    username = forms.CharField(label='Write your user name')
    email = forms.EmailField(label='Write your email')
    password1 = forms.CharField(label='Create passwor')
    password2 = forms.CharField(label='Repeate password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class EditProfileForm(BulmaMixin, forms.ModelForm):
    email = forms.EmailField(label='Write your email')
    first_name = forms.CharField(label='Write your first name')
    last_name = forms.CharField(label='Write your last name')
    username = forms.CharField(label='Write your user name')


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']



class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')


    class Meta:
        model = User
        fields = ['username', 'password']


class ChangePasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.CharField()  
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']      

        