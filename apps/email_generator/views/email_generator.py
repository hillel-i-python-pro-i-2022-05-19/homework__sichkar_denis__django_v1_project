from typing import ClassVar

from django.views.generic import TemplateView

from apps.email_generator.services import users_generator


class EmailGeneratorView(TemplateView):
    template_name = 'email_generator/show_email.html'
    _DEFAULT_NUMBER_OF_EMAIL: ClassVar[int] = 100

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        try:
            email_length = data["email_length"]
        except KeyError:
            email_length = 100
            data['email_length'] = email_length
        user_as_list = users_generator(email_length)
        new_users = [f'''{user.name} {user.email}''' for user in user_as_list]
        data['new_users'] = new_users
        data['email_length'] = len(new_users)
        return data

# def email_generator(request: HttpRequest, amount: int = 100) -> HttpResponse:
#     user_as_list = users_generator(amount)
#     new_users = [f'''{user.name} {user.email}''' for user in user_as_list]
#     email_length = len(new_users)
#     return render(request, 'email_generator/show_email.html', {"new_users": new_users, "email_length": email_length})


# class PasswordGeneratorView(TemplateView):
#     template_name = 'password_generator/show_password.html'
#     _DEFAULT_PASSWORD_LENGTH: ClassVar[int] = 10
#
#     def get_context_data(self, **kwargs):
#         # [init] - [BEGIN]
#         data = super().get_context_data(**kwargs)
#
#         try:
#             password_length = data["password_length"]
#         except KeyError:
#             password_length = 10
#             data['password_length'] = password_length
#         # [init] - [END]
#         # [action] - [BEGIN]
#         password = generate_password(password_length=password_length)
#         # [action] - [END]
#         data['password'] = password
#         return data
