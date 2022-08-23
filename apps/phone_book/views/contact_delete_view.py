from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.phone_book.models import Contact


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:show_contacts')
