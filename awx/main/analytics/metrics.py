import os
from datetime import datetime

from prometheus_client import (
    Gauge,
    Info
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
from awx.main.analytics.collectors import counts
from django.contrib.sessions.models import Session
from awx.main.analytics import register


SYSTEM_INFO = Info('awx_system_info', 'AWX System Information')
TOTAL_SESSIONS = Guage('awx_active_sessions', 'Number of active session')
CUSTOM_VENVS = Guage('awx_custom_virtualenvs', 'Number of virtualenvs')
ORG_COUNT = Guage('awx_organizations', 'Number of organizations')
USER_COUNT = Guage('awx_users', 'Number of users')
TEAM_COUNT = Guage('awx_teams', 'Number of teams')
INV_COUNT = Guage('awx_inventories', 'Number of inventories')
PROJ_COUNT = Guage('awx_projects', 'Number of projects')
JT_COUNT = Guage('awx_job_templates', 'Number of job templates')
WFJT_COUNT = Guage('awx_workflow_job_templates', 'Number of workflow job templates')
HOST_COUNT = Guage('awx_hosts', 'Number of hosts')
SCHEDULE_COUNT = Guage('awx_schedules', 'Number of schedules')
INV_SCRIPT_COUNT = Guage('awx_inventory_scripts', 'Number of invetory scripts'

def metrics():
    license_info = get_license(show_key=False)
    SYSTEM_INFO.info({'system_uuid': settings.SYSTEM_UUID, 
                      'tower_url_base': settings.TOWER_URL_BASE,
                      'tower_version': get_awx_version(),
                      'ansible_version': get_ansible_version(),
                      'license_type': license_info.get('license_type', 'UNLICENSED'),
                      'free_instances': str(license_info.get('free instances', 0)),
                      'license_expiry': str(license_info.get('time_remaining', 0)),
                      'pendo_tracking': settings.PENDO_TRACKING_STATE,
                      'external_logger_enabled': str(settings.LOG_AGGREGATOR_ENABLED),
                      'external_logger_type': getattr(settings, 'LOG_AGGREGATOR_TYPE', 'None')})

    current_counts = counts(datetime.now()) 

    CUSTOM_VENS.set(current_counts['custom_virtualenvs'])
    TOTAL_SESSIONS.set(current_counts['active_sessions'])

    return generate_latest()


__all__ = ['metrics']
