from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    repassword = forms.CharField(
        label="Repeat password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def clean_repassword(self):
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")
        if len(password) < 5:
            self.add_error(
                "password", "Password length must be greater than 5 characters"
            )
            return

        if password != repassword:
            self.add_error(
                "repassword", "Password and repeat password are not the same"
            )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "gender")


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Username or password is incorrect")
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label="Current password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    new_password = forms.CharField(
        label="New password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class EmailVerificationForm(forms.Form):
    code = forms.CharField(
        label="Verification code",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
