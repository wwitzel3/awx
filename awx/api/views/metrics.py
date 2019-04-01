# Copyright (c) 2018 Red Hat, Inc.
# All Rights Reserved.

# Python
import logging

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

# Django REST Framework
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer

# AWX
# from awx.main.analytics import collectors
from awx.main.analytics.metrics import metrics
from awx.api import renderers

from awx.api.generics import (
    APIView,
)

from awx.api.serializers import (
    InventorySerializer,
    ActivityStreamSerializer,
)

logger = logging.getLogger('awx.main.analytics')



class MetricsView(APIView):

    view_name = _('Metrics')
    swagger_topic = 'Metrics'
    
    renderer_classes = [renderers.PlainTextRenderer]
                        # renderers.BrowsableAPIRenderer,  # TODO: Add back in
                        # JSONRenderer]
    
    def get(self, request, format='txt'):
        ''' Show Metrics Details '''
        
        # # Temporary Imports
        from awx.main.models.organization import UserSessionMembership
        from django.contrib.sessions.models import Session
        
        # Add active/expired, or only query active sessions
        total_sessions = Session.objects.all().count()
        
        # Placeholder data below for testing against Prometheus
        # will ultimately reformat and re-use much of the analytics data
        
        data = []
        data.append("# HELP awx_sessions_active counter A count of active sessions.")
        data.append("# TYPE awx_sessions_active counter")
        data.append("awx_sessions_active_sessions {0} ".format(str(total_sessions)))

        
        # return Response(metrics().decode("utf-8"))
        return Response("\n".join(data))