from django.db import models


class SessionAll(models.Model):
    session_key = models.CharField(
        "Session key",
        help_text="Key of Session",
        max_length=1000,
    )
    count_of_visits = models.PositiveSmallIntegerField(
        name="count_of_visits",
    )
    last_visit = models.DateTimeField(
        name="last_visit",
    )
