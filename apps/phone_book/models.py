from birthday import BirthdayField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible
from phonenumber_field.modelfields import PhoneNumberField


class Tag(models.Model):
    name = models.CharField(
        'Name',
        help_text='Name of tag',
        max_length=200,
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__


@deconstructible
class RequireLinkToLinkedinProfile:
    def __call__(self, value):
        if not value.startswith("https://www.linkedin.com/in/"):
            raise ValidationError('The link must start with "https://www.linkedin.com/in/"')
        elif len(value) < 29:
            raise ValidationError('Enter full link')


class PhoneBook(models.Model):
    contact_name = models.CharField(
        "Contact name",
        help_text='This is the name of the contact',
        null=False,
        blank=False,
        max_length=200
    )
    contact_birthday = BirthdayField(
        "Birthday",
        help_text='This is the birthday of the contact',
        null=True,
        blank=True,
        max_length=150,
    )

    phone_number = PhoneNumberField(
        "Phone number",
        help_text='This is a phone number',
        null=False,
        blank=False,
        unique=True,

    )
    url_profile_linkedin = models.URLField(
        "LinkedIn Url profile",
        help_text='Link to LinkedIn Profile',
        null=False,
        blank=False,
        validators=[RequireLinkToLinkedinProfile()],
    )
    nick_linkedin = models.CharField(
        "linkedin Nick",
        help_text='Automatically generated from LinkedIn Url profile',
        null=True,
        blank=True,
        max_length=200,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='Contact_related_many_to_many_items',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.nick_linkedin = self.url_profile_linkedin.split("https://www.linkedin.com/in/")[1]
        if self.nick_linkedin[-1:] == '/':
            self.nick_linkedin = self.nick_linkedin[:-1]
        super().save(force_insert, force_update)

    def __str__(self) -> str:
        return f"{self.contact_name} - {self.phone_number}"

    __repr__ = __str__


class ContactDetails(models.Model):
    id_phone_book = models.ForeignKey(
        PhoneBook,
        verbose_name='Contact',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    contact_details_name = models.CharField(
        'Contact details name',
        help_text='Name of contact details',
        max_length=200,
    )
    contact_details = models.CharField(
        "Contact details",
        help_text='This is the contact details',
        max_length=200
    )

    def __str__(self) -> str:
        return f"{self.id_phone_book.contact_name}: {self.contact_details_name} - {self.contact_details}"

    __repr__ = __str__
