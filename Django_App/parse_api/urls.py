from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("show/", views.show),
    path("logout/", views.logout_view),
    path("register/", views.registrate),
    path("create_post/",views.create_post)
]
