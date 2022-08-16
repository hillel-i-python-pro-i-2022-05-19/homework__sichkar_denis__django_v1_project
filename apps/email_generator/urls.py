from django.urls import path

from . import views

app_name = "email_generator"

urlpatterns = [
    path("", views.email_generator, name='index'),
    path('<int:amount>', views.email_generator),
]
