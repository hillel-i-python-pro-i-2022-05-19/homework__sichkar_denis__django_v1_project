from django.contrib import admin

from apps.middleware_logger.models import RequestLog


@admin.register(RequestLog)
class LogAdmin(admin.ModelAdmin):
    ...
