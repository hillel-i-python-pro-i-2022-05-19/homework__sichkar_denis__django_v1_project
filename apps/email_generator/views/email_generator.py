from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from apps.email_generator.services import users_generator


def email_generator(request: HttpRequest, amount: int = 100) -> HttpResponse:
    user_as_list = users_generator(amount)
    new_users = [f'''{user.name} {user.email}''' for user in user_as_list]
    email_length = len(new_users)
    return render(request, 'email_generator/show_email.html', {"new_users": new_users, "email_length": email_length})
