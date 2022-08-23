from django.urls import path

from . import views

app_name = "email_generator"

urlpatterns = [
    path("", views.EmailGeneratorView.as_view(), name='index'),
    path('<int:amount>', views.EmailGeneratorView.as_view()),
]
