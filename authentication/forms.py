from django import forms


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=13, min_length=13)
    password = forms.CharField(max_length=128)


class RegisterForm(forms.Form):
    phone_number = forms.CharField(max_length=13, min_length=13)
    password = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)
