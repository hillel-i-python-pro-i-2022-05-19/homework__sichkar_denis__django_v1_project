from django import forms

from apps.phone_book.models import Contact

BIRTH_YEAR_CHOICES = list(range(1850, 2023)[::-1])


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "contact_name",
            "contact_birthday",
            "tags",
        ]

    contact_birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
