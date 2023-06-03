from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import UserAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login, logout


class LoginView(View):
    form_class = UserAuthenticationForm
    template_name = "account/login.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print("Login Successfull")
            return redirect("home_page")
        context = {"form": form}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect("home_page")


class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = "account/register.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            print("User Created Successfull...")
            return redirect("LoginView")
        context = {"form": form}
        print("Something Wrong...")
        return render(request, self.template_name, context)
