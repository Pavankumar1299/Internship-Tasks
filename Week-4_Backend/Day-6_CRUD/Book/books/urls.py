from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update/<int:id>/", views.update_book, name="update_book"),
    path("delete/<int:id>/", views.delete_book, name="delete_book"),
]