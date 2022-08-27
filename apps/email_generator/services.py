import collections
from collections.abc import Iterator

from apps.email_generator.utils import generator_name, generator_email

User = collections.namedtuple("User", ["name", "email"])


def user_generator() -> User:
    return User(name=generator_name(), email=generator_email())


def users_generator(amount) -> Iterator[User]:
    for _ in range(amount):
        yield user_generator()
