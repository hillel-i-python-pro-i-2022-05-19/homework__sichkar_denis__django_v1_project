import re
import uuid

from birthday import BirthdayField
from django import forms
from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(
        "Name",
        help_text="Name of tag",
        max_length=200,
    )

    def __str__(self) -> str:
        return f"{self.tag_name}"

    __repr__ = __str__


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"humans/avatars/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contact(models.Model):
    contact_name = models.CharField(
        "Contact name", help_text="This is the name of the contact", null=False, blank=False, max_length=200
    )
    contact_birthday = BirthdayField(
        "Birthday", help_text="This is the birthday of the contact", null=True, blank=True, max_length=150
    )
    tags = models.ManyToManyField(Tag, related_name="Contact_related_many_to_many_items", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(
        "Avatar",
        upload_to=get_icon_path,
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.contact_name}"

    __repr__ = __str__


class ContactTypeChoice(models.TextChoices):
    PHONE = "PHONE", "Phones"
    EMAIL = "EMAIL", "Email"
    TELEGRAM = "TELEGRAM", "Telegram"
    LINKEDIN = "LINKEDIN", "Linkedin"


class ContactDetail(models.Model):  # Contact
    user = models.ForeignKey(
        "Contact",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    contact_detail_type = models.CharField(
        "Contact details name",
        help_text="Type of contact details",
        max_length=200,
        choices=ContactTypeChoice.choices,
        default=ContactTypeChoice.PHONE,
    )
    contact_detail_value = models.CharField("Contact details", help_text="This is the contact details", max_length=200)

    def clean(self):
        regex_to_types = {
            "PHONE": r"^(?:0|\+?380)\s?(?:\d\s?){9}$",
            "EMAIL": r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
            "TELEGRAM": r".*\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*.*$",
            "LINKEDIN": r"^https?://((www|\w\w)\.)?linkedin.com/((in/[^/]+/?)|(pub/[^/]+/((\w|\d)+/?){3}))$",
        }
        if not re.search(regex_to_types[self.contact_detail_type], self.contact_detail_value):
            raise forms.ValidationError("Incorrect Value")
        return self.contact_detail_value

    def __str__(self) -> str:
        return f"{self.user.contact_name}: {self.contact_detail_type} - {self.contact_detail_value}"

    __repr__ = __str__
