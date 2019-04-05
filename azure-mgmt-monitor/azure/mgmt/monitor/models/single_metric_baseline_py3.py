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


class SingleMetricBaseline(Model):
    """The baseline results of a single metric.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The metric baseline Id.
    :type id: str
    :param type: Required. The resource type of the metric baseline resource.
    :type type: str
    :param name: Required. The name of the metric for which the baselines were
     retrieved.
    :type name: str
    :param timespan: Required. The timespan for which the data was retrieved.
     Its value consists of two datetimes concatenated, separated by '/'.  This
     may be adjusted in the future and returned back from what was originally
     requested.
    :type timespan: str
    :param interval: Required. The interval (window size) for which the metric
     data was returned in.  This may be adjusted in the future and returned
     back from what was originally requested.  This is not present if a
     metadata request was made.
    :type interval: timedelta
    :param namespace: The namespace of the metrics been queried.
    :type namespace: str
    :param baselines: Required. The baseline for each time series that was
     queried.
    :type baselines: list[~azure.mgmt.monitor.models.TimeSeriesBaseline]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'name': {'required': True},
        'timespan': {'required': True},
        'interval': {'required': True},
        'baselines': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'timespan': {'key': 'properties.timespan', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'duration'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'baselines': {'key': 'properties.baselines', 'type': '[TimeSeriesBaseline]'},
    }

    def __init__(self, *, id: str, type: str, name: str, timespan: str, interval, baselines, namespace: str=None, **kwargs) -> None:
        super(SingleMetricBaseline, self).__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.timespan = timespan
        self.interval = interval
        self.namespace = namespace
        self.baselines = baselines
