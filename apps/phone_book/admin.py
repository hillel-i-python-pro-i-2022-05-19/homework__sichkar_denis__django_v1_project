from django.contrib import admin

from .models import Contact, Tag, ContactDetail, ContactTypeChoice


class ContactDetailInlineAdmin(admin.TabularInline):
    model = ContactDetail
    max_num = len(ContactTypeChoice)


@admin.register(Contact)
class PhoneBookAdmin(admin.ModelAdmin):
    inlines = [ContactDetailInlineAdmin]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    ...
