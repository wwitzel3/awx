import os

from prometheus_client import (
    Gauge, Info, Counter,
    generate_latest
)

from django.contrib.sessions.models import Session

# Temporary Imports 
from django.db import connection
from django.db.models import Count
from django.conf import settings

from awx.conf.license import get_license
from awx.main.utils import (get_awx_version, get_ansible_version,
                            get_custom_venv_choices)
from awx.main import models
from django.contrib.sessions.models import Session
from awx.main.analytics import register


def metrics():

    system_info = Info('awx_systemuuid', 'System_UUID of the Tower System')
    license_info = get_license(show_key=False)
    system_info.info({'system_uuid': settings.SYSTEM_UUID, 
                      'tower_url_base': settings.TOWER_URL_BASE,
                      'tower_version': get_awx_version(),
                      'ansible_version': get_ansible_version(),
                      'license_type': license_info.get('license_type', 'UNLICENSED'),
                      'free_instances': str(license_info.get('free instances', 0)),
                      'license_expiry': str(license_info.get('time_remaining', 0)),
                      'pendo_tracking': settings.PENDO_TRACKING_STATE,
                      'external_logger_enabled': str(settings.LOG_AGGREGATOR_ENABLED),
                      'external_logger_type': getattr(settings, 'LOG_AGGREGATOR_TYPE', 'None')})
    
    venvs = get_custom_venv_choices()
    custom_virtualenvs = Gauge('awx_custom_virtualenvs', 'Number of virtualenvs')
    num_custom_virtualenvs = len([
        v for v in venvs
        if os.path.basename(v.rstrip('/')) != 'ansible'
    ])
    
    
    
    total_sessions = Gauge('awx_totalsessions', 'Total active session count')
    total_sessions.set_function(lambda: Session.objects.all().count())

    return generate_latest()
    