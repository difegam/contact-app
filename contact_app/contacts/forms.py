import typing

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Form for creating and updating contacts."""

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "is_favorite",
        )
        widgets: typing.ClassVar = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone"}),
            "address": forms.Textarea(attrs={"placeholder": "Address"}),
        }
        labels: typing.ClassVar = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "phone": "Phone",
            "address": "Address",
            "is_favorite": "Favorite",
        }
        help_texts: typing.ClassVar = {
            "first_name": "Enter the first name of the contact.",
            "last_name": "Enter the last name of the contact.",
            "email": "Enter a valid email address.",
            "phone": "Enter the phone number.",
            "address": "Enter the address.",
        }
