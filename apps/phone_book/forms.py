from django import forms

from apps.phone_book.models import PhoneBook, ContactDetails

BIRTH_YEAR_CHOICES = list(range(1850, 2023)[::-1])


class ContactsForm(forms.ModelForm):
    class Meta:
        model = PhoneBook
        fields = ["contact_name", "phone_number", 'nick_linkedin', 'contact_birthday', "tags"]

    contact_birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))


class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ["contact_details_name", "contact_details"]
