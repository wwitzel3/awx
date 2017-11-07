# Copyright (c) 2016 Ansible, Inc.
# All Rights Reserved.

from awx.api.urls import scoped_url


url = scoped_url('awx.conf.views')

urlpatterns = [ 
    url(r'^$', 'setting_category_list'),
    url(r'^(?P<category_slug>[a-z0-9-]+)/$', 'setting_singleton_detail'),
    url(r'^logging/test/$', 'setting_logging_test'),
]
