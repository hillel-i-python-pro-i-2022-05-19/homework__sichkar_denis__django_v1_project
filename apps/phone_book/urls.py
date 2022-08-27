from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactListView.as_view(), name="show_contacts"),
    path("create_contact", views.create_contact, name="create_contact"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit_contact", views.ContactEditView.as_view(), name="edit_contact"),
                path("delete_contact", views.ContactDeleteView.as_view(), name="delete_contact"),
            ]
        ),
    ),
]
