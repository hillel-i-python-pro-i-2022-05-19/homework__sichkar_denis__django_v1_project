from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.phone_book.models import PhoneBook


class ContactEditView(UpdateView):
    model = PhoneBook
    fields = ["contact_name", "phone_number", 'contact_birthday', "tags"]
    success_url = reverse_lazy('contacts:show_contacts')
