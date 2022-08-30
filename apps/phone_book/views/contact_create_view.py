from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from apps.phone_book.forms import ContactsForm


@login_required
def create_contact(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Contact created")
            return redirect("contacts:show_contacts")
    else:
        form = ContactsForm()
    return render(request, "phone_book/contact_form.html", {"form": form})
