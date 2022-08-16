from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class PhoneBook(models.Model):
    contact_name = models.CharField("Contact name", help_text='This is the name of the contact', max_length=200)
    phone_number = PhoneNumberField(
        "Phone number",
        help_text='This is a phone number',
        null=False,
        blank=False,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
