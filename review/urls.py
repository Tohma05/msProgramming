from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.chapter, name="chapter"),
    path("chap1/", views.chap1, name="chap1"),
    path("zero/", views.zero, name="zero"),
]