from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactListView.as_view(), name="show_contacts"),
    path("create_contact", views.ContactCreateView.as_view(), name="create_contact"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit_contact", login_required(views.ContactEditView.as_view()), name="edit_contact"),
                path("delete_contact", login_required(views.ContactDeleteView.as_view()), name="delete_contact"),
            ]
        ),
    ),
]
