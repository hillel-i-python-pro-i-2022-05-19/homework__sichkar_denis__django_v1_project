from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.phone_book.models import Contact


class ContactEditView(UpdateView):
    model = Contact
    fields = ["contact_name", 'contact_birthday', "tags"]
    success_url = reverse_lazy('contacts:show_contacts')
