from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="Account", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="Password", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    # captcha = CaptchaField(label='Verification code')


class RegisterForm(forms.Form):
    Role = (
        ('student', "Student"),
        ('teacher', "Teacher"),
    )
    username = forms.CharField(label="Account", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(label='Role', choices=Role)
    # captcha = CaptchaField(label='Verification code')


class AccountProfileForm(forms.Form):
    Gender = (
        ('male', "Male"),
        ('female', "Female"),
        ('none', "None"),
    )
    firstname = forms.CharField(label="firstname", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label="lastname", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="email", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='Gender', choices=Gender)
    organization = forms.CharField(label="orgnization", max_length=256,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='Verification code')
