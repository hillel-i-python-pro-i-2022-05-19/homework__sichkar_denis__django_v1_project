from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.phone_book.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = ["contact_name", "contact_birthday", "tags"]
    template_name = "phone_book/contact_form.html"
    success_url = reverse_lazy("contacts:show_contacts")
