from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.phone_book.models import PhoneBook


class ContactDeleteView(DeleteView):
    model = PhoneBook
    success_url = reverse_lazy('contacts:show_contacts')
