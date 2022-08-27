from faker import Faker

fake = Faker()


def generator_name() -> str:
    return fake.unique.first_name()


def generator_email() -> str:
    return fake.unique.ascii_email()
