from django import forms

from apps.phone_book.models import PhoneBook


class ContactsForm(forms.ModelForm):
    class Meta:
        model = PhoneBook
        fields = ("contact_name","phone_number",)