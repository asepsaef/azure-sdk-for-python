# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LabAnnouncementPropertiesFragment(Model):
    """Properties of a lab's announcement banner.

    :param title: The plain text title for the lab announcement
    :type title: str
    :param markdown: The markdown text (if any) that this lab displays in the
     UI. If left empty/null, nothing will be shown.
    :type markdown: str
    :param enabled: Is the lab announcement active/enabled at this time?.
     Possible values include: 'Enabled', 'Disabled'
    :type enabled: str or ~azure.mgmt.devtestlabs.models.EnableStatus
    :param expiration_date: The time at which the announcement expires (null
     for never)
    :type expiration_date: datetime
    :param expired: Has this announcement expired?
    :type expired: bool
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'markdown': {'key': 'markdown', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'str'},
        'expiration_date': {'key': 'expirationDate', 'type': 'iso-8601'},
        'expired': {'key': 'expired', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(LabAnnouncementPropertiesFragment, self).__init__(**kwargs)
        self.title = kwargs.get('title', None)
        self.markdown = kwargs.get('markdown', None)
        self.enabled = kwargs.get('enabled', None)
        self.expiration_date = kwargs.get('expiration_date', None)
        self.expired = kwargs.get('expired', None)
