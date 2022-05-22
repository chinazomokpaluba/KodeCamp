from django.urls import path
from .views import about, home,contact

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
]