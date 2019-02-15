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


class KnowledgebasesDTO(Model):
    """Collection of knowledgebases owned by a user.

    :param knowledgebases: Collection of knowledgebase records.
    :type knowledgebases:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.KnowledgebaseDTO]
    """

    _attribute_map = {
        'knowledgebases': {'key': 'knowledgebases', 'type': '[KnowledgebaseDTO]'},
    }

    def __init__(self, **kwargs):
        super(KnowledgebasesDTO, self).__init__(**kwargs)
        self.knowledgebases = kwargs.get('knowledgebases', None)
