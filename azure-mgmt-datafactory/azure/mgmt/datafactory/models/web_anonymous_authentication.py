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

from .web_linked_service_type_properties import WebLinkedServiceTypeProperties


class WebAnonymousAuthentication(WebLinkedServiceTypeProperties):
    """A WebLinkedService that uses anonymous authentication to communicate with
    an HTTP endpoint.

    All required parameters must be populated in order to send to Azure.

    :param url: Required. The URL of the web service endpoint, e.g.
     http://www.microsoft.com . Type: string (or Expression with resultType
     string).
    :type url: object
    :param authentication_type: Required. Constant filled by server.
    :type authentication_type: str
    """

    _validation = {
        'url': {'required': True},
        'authentication_type': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'object'},
        'authentication_type': {'key': 'authenticationType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WebAnonymousAuthentication, self).__init__(**kwargs)
        self.authentication_type = 'Anonymous'
