import datetime
from typing import Any, ClassVar

from django.views.generic import TemplateView

from .models import SessionAll


class SessionExample(TemplateView):
    template_name = "sessions_example/index.html"
    KEY_TO_COUNT_OF_VISITS: ClassVar[str] = "count_of_visits"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        session = self.request.session
        count_of_visits = session.get(self.KEY_TO_COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[self.KEY_TO_COUNT_OF_VISITS] = count_of_visits
        kwargs[self.KEY_TO_COUNT_OF_VISITS] = count_of_visits
        kwargs["session_id"] = session.session_key
        if count_of_visits > 1:
            last_visit = datetime.datetime.now()
            if SessionAll.objects.filter(session_key=session.session_key).exists():
                SessionAll.objects.filter(session_key=session.session_key).update(
                    count_of_visits=count_of_visits, last_visit=last_visit
                )
            else:
                SessionAll.objects.create(
                    session_key=session.session_key, count_of_visits=count_of_visits, last_visit=last_visit
                )
            kwargs["last_visit"] = SessionAll.objects.get(session_key=session.session_key).last_visit
        return kwargs
