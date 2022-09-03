from django import forms

class Signup (forms.Form):
    name = forms.CharField(label = "Name", max_length = 100)
    regno = forms.CharField(label = "Registration Number", max_length = 10)
    passw = forms.CharField(label = "Password", widget = forms.PasswordInput())
    cpassw = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput())

class Login (forms.Form):
    regno = forms.CharField(label="Registration Number", max_length=10)
    passw = forms.CharField(label="Password", widget=forms.PasswordInput())