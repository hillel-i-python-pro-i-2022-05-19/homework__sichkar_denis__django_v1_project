import datetime
import logging
from collections.abc import Callable
from typing import ClassVar

from django.utils import timezone

from apps.middleware_logger.models import RequestLog


class SimpleLoggingMiddleware:
    _NAME: ClassVar[str] = "first"

    def __init__(self, get_response: Callable):
        """One-time configuration and initialization."""
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        message = f"[{self._NAME}] {request.path} {request.user.is_authenticated} {request.user}"
        self.logger.info(f"[before] {message}")

        # Get resp
        response = self.get_response(request)

        if RequestLog.objects.filter(user=request.user, request_path=request.path).exists():
            request_log = RequestLog.objects.get(user=request.user, request_path=request.path)
            update_request_count = request_log.request_count + 1
            RequestLog.objects.filter(user=request.user, request_path=request.path).update(
                request_count=update_request_count, last_visit=datetime.datetime.now(tz=timezone.utc)
            )
            self.logger.info(
                f"[Update log] User: {request_log.user} "
                f" Path: {request_log.request_path}"
                f" Request count: {request_log.request_count}"
            )
        else:
            RequestLog.objects.create(user=request.user, request_path=request.path)
            request_log = RequestLog.objects.get(user=request.user, request_path=request.path)
            self.logger.info(
                f"[Create log] User: {request_log.user}"
                f" Path: {request_log.request_path}"
                f" Request count: {request_log.request_count}"
            )

        # Code to be executed for each request/response after the view is called.
        self.logger.info(f"[after] {message}")

        return response


class SimpleLoggingMiddleware2(SimpleLoggingMiddleware):
    _NAME: ClassVar[str] = "second"
