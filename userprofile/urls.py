from django.urls import path
from userprofile import views

app_name = "userprofile"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),

]