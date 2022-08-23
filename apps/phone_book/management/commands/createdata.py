import random

from django.core.management.base import BaseCommand
from faker import Faker
from nickname_generator import generate

from apps.phone_book.models import Contact, Tag, ContactDetail, ContactTypeChoice


class Command(BaseCommand):
    help = "Command information"
    fake = Faker()

    def generator_random_numbers(self) -> int:
        return random.randint(100000000, 999999999)

    def generator_name(self) -> str:
        first_name = self.fake.first_name()
        return first_name

    def generator_email(self) -> str:
        email = self.fake.email()
        return email

    def generator_telegram_nick(self) -> str:
        return f'@{generate()}'

    def generate_url_profile_linkedin(self, first_name) -> str:
        random_numbers = self.generator_random_numbers()
        last_name = self.fake.last_name()
        return f"https://www.linkedin.com/in/{first_name.lower()}-{last_name.lower()}-{random_numbers}a1/"

    def generate_phone_number(self) -> str:
        random_numbers = self.generator_random_numbers()
        return f'+380{random_numbers}'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            contact_birthday = self.fake.date_of_birth(minimum_age=18, maximum_age=99)
            phone_number = self.generate_phone_number()
            contact_name = self.generator_name()
            email = self.generator_email()
            url_profile_linkedin = self.generate_url_profile_linkedin(contact_name)
            telegram_nick = self.generator_telegram_nick()
            new_contact = Contact.objects.create(
                contact_name=contact_name,
                contact_birthday=contact_birthday,
            )
            for value in ContactTypeChoice.choices[:random.randint(0, 4)]:
                contact_detail_type = 'PHONE'
                contact_detail_value = ''
                if 'PHONE' in value:
                    contact_detail_value = phone_number
                elif 'EMAIL' in value:
                    contact_detail_type = 'EMAIL'
                    contact_detail_value = email
                elif 'TELEGRAM' in value:
                    contact_detail_type = 'TELEGRAM'
                    contact_detail_value = telegram_nick
                elif 'LINKEDIN' in value:
                    contact_detail_type = 'LINKEDIN'
                    contact_detail_value = url_profile_linkedin
                ContactDetail.objects.create(
                    id_contact=new_contact,
                    contact_detail_type=contact_detail_type,
                    contact_detail_value=contact_detail_value,
                )

        for _ in range(5):
            word = self.fake.word()
            Tag.objects.create(
                tag_name=word
            )

        check_contacts = Contact.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of contacts: {check_contacts}"))
