from django.views.generic import ListView

from apps.phone_book.models import PhoneBook


class ContactListView(ListView):
    model = PhoneBook
