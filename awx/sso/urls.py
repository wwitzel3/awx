# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

from awx.api.urls import scoped_url


url = scoped_url('awx.sso.views')

urlpatterns = [
    url(r'^complete/$', 'sso_complete', name='sso_complete'),
    url(r'^error/$', 'sso_error', name='sso_error'),
    url(r'^inactive/$', 'sso_inactive', name='sso_inactive'),
    url(r'^metadata/saml/$', 'saml_metadata', name='saml_metadata'),
]
