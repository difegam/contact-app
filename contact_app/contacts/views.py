# Create your views here.
# contact_list, contact_detail, contact_create, contact_update, contact_delete
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "contacts/home.html", {})


def contact_list(request: HttpRequest) -> HttpResponse:
    """Display a list of contacts."""
    # Get the search query from the request
    search = request.GET.get("q", "")
    print("Search query:", search)
    # Filter contacts based on the search query or show all contacts
    search_query = Q(first_name__icontains=search) | Q(last_name__icontains=search)
    contacts = Contact.objects.filter(search_query) if search else Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


def contact_create(request: HttpRequest) -> HttpResponse:
    """Create a new contact."""
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Save the new contact to the database
        form.save()
        return redirect("contacts:contact-list")
    return render(request, "contacts/contact_create.html", {"form": form})
