from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from apps.phone_book.forms import ContactsForm
from apps.phone_book.models import PhoneBook


def show_contacts(request: HttpRequest) -> HttpResponse:
    phone_book = PhoneBook.objects.all()
    return render(request, 'phone_book/show_contacts.html', {"phone_book": phone_book, })


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Contact created")
            return redirect('contacts:show_contacts')
    else:
        form = ContactsForm()
    return render(request, 'phone_book/create_contact.html', {"form": form})


def edit_contact(request: HttpRequest, pk) -> HttpResponse:
    phone_book = get_object_or_404(PhoneBook, pk=pk)
    if request.POST:
        form = ContactsForm(request.POST, instance=phone_book)
        if form.is_valid():
            form.save()
            messages.info(request, "Contact changed")
            return redirect('contacts:show_contacts')
    else:
        form = ContactsForm(instance=phone_book)
    return render(request, 'phone_book/create_contact.html', {"form": form})


def delete_contact(request: HttpRequest, pk) -> HttpResponse:
    total_deleted, _ = PhoneBook.objects.filter(pk=pk).delete()
    if total_deleted:
        messages.info(request, "Contact deleted")
    else:
        messages.info(request, "Nothing deleted")
    return redirect("contacts:show_contacts")
