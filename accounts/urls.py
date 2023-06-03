from django.urls import path
from accounts import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="LoginView"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.RegisterView.as_view(), name="RegisterView"),
]
