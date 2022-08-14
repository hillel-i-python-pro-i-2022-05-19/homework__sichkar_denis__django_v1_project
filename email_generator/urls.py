from django.urls import path

from . import views

urlpatterns = [
    path('', views.emails_generator),
    path('<int:amount>', views.emails_generator),
]