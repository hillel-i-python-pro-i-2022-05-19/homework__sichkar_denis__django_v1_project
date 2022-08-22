import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.phone_book.models import PhoneBook, Tag, ContactDetails


class Command(BaseCommand):
    help = "Command information"

    def generate_random_numbers(self):
        return random.randint(10000000, 99999999)

    def generate_url_profile_linkedin(self):
        fake = Faker()
        self.first_name = fake.first_name()
        last_name = fake.last_name().lower()
        random_numbers = self.generate_random_numbers()
        return f"https://www.linkedin.com/in/{self.first_name.lower()}-{last_name}-{random_numbers}a1/"

    def generate_phone_number(self):
        random_numbers = self.generate_random_numbers()
        return f'+121{random_numbers}'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(5):
            contact_birthday = fake.date_of_birth(minimum_age=18, maximum_age=99)
            phone_number = self.generate_phone_number()
            url_profile_linkedin = self.generate_url_profile_linkedin()
            new_contact = PhoneBook.objects.create(
                contact_name=self.first_name,
                contact_birthday=contact_birthday,
                phone_number=phone_number,
                url_profile_linkedin=url_profile_linkedin,
            )
            for _ in range(random.randint(3, 6)):
                ContactDetails.objects.create(
                    id_phone_book=new_contact,
                    contact_details_name=fake.first_name().lower(),
                    contact_details=fake.first_name().lower()

                )

        for _ in range(5):
            name = fake.word()
            Tag.objects.create(
                name=name
            )

        check_contacts = PhoneBook.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of contacts: {check_contacts}"))
