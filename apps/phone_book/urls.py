from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_contacts, name='show_contacts'),
    path("create_contact", views.create_contact, name='create_contact'),
    path("<int:pk>/", include([
        path("edit_ontact", views.edit_contact, name='edit_contact'),
        path("delete_contact", views.delete_contact, name='delete_contact'),
    ])),
]
