from django.urls import path

from .views import contact_create, contact_list, home

app_name = "contacts"

# URL patterns for the contacts app
urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact_list, name="contact-list"),
    path("contacts/new/", contact_create, name="contact-create"),
]
