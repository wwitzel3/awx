# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

from awx.api.urls import scoped_url


url = scoped_url('awx.ui.views')

urlpatterns = [ 
    url(r'^$', 'index', name='index'),
    url(r'^migrations_notran/$', 'migrations_notran', name='migrations_notran'),
    url(r'^portal/$', 'portal_redirect', name='portal_redirect'),
]
