from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.user_form, name="form"),
    path("login/", views.login_form, name="login"),
    # path("success/", views.user_list, name="success"),
]