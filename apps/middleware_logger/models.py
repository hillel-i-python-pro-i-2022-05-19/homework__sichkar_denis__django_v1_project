import datetime

from django.db import models
from django.utils import timezone


class RequestLog(models.Model):
    user = models.CharField("User", max_length=200)
    request_path = models.CharField("Request Path", max_length=200)
    request_count = models.PositiveIntegerField("Number of requests", default=1)
    last_visit = models.DateTimeField(
        "Last Visit", null=True, blank=True, default=datetime.datetime.now(tz=timezone.utc)
    )

    def __str__(self):
        return f"{self.user} ({self.request_path})"

    __repr__ = __str__
