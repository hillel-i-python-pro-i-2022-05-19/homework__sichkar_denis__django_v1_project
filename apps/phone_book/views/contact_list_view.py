from django.views.generic import ListView

from apps.phone_book.models import Contact


class ContactListView(ListView):
    model = Contact
