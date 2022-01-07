from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .forms import (
    UserRegisterForm,
    LoginForm,
    UpdatePasswordForm,
    EmailVerificationForm,
)
from .models import User
from .functions import code_generator


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        register_code = code_generator()
        User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            gender=form.cleaned_data["gender"],
            register_code=register_code,
        )

        subject = "Confirmation email"
        message = f"Verification code: {register_code}"
        sender = "eliashhtorres@gmail.com"
        send_mail(subject, message, sender, [form.cleaned_data["email"]])

        return redirect(reverse("users_app:verify"))


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home_app:panel")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("users_app:login"))


class UpdatePasswordView(LoginRequiredMixin, FormView):
    login_url = "users_app:login"
    template_name = "users/update_password.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy("users_app:login")

    def form_valid(self, form):
        user = self.request.user
        auth = authenticate(
            username=user.username,
            password=form.cleaned_data["password"],
        )
        if auth:
            user.set_password(form.cleaned_data["new_password"])
            user.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class CodeVerificationView(FormView):
    template_name = "users/code_verification.html"
    form_class = EmailVerificationForm
    success_url = reverse_lazy("users_app:login")

    def form_valid(self, form):

        return super(CodeVerificationView, self).form_valid(form)
