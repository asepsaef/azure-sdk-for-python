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


class BaseImageTriggerUpdateParameters(Model):
    """The properties for updating base image dependency trigger.

    All required parameters must be populated in order to send to Azure.

    :param base_image_trigger_type: The type of the auto trigger for base
     image dependency updates. Possible values include: 'All', 'Runtime'
    :type base_image_trigger_type: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.BaseImageTriggerType
    :param status: The current status of trigger. Possible values include:
     'Disabled', 'Enabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.TriggerStatus
    :param name: Required. The name of the trigger.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'base_image_trigger_type': {'key': 'baseImageTriggerType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name: str, base_image_trigger_type=None, status=None, **kwargs) -> None:
        super(BaseImageTriggerUpdateParameters, self).__init__(**kwargs)
        self.base_image_trigger_type = base_image_trigger_type
        self.status = status
        self.name = name
