from django.contrib import admin

from .models import PhoneBook, Tag, ContactDetails


class ContactDetailsInlineAdmin(admin.TabularInline):
    model = ContactDetails


@admin.register(PhoneBook)
class PhoneBookAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailsInlineAdmin
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    ...
