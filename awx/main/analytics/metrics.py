from prometheus_client import (
    Gauge,
    generate_latest,
)

from django.contrib.sessions.models import Session
     
def metrics():
    total_sessions = Gauge('awx_total_sessions', 'Total active session count')
    total_sessions.set_function(lambda: Session.objects.all().count())

    return generate_latest()