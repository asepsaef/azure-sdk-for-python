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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from .version import VERSION


class KeyVaultClientConfiguration(AzureConfiguration):
    """Configuration for KeyVaultClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    """

    def __init__(
            self, credentials):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{vaultBaseUrl}'

        super(KeyVaultClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-keyvault/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class KeyVaultClient(MultiApiClientMixin):
    """The key vault client performs cryptographic key operations and vault operations against the Key Vault service.

    :ivar config: Configuration for client.
    :vartype config: KeyVaultClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`

    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '7.0'
    _PROFILE_TAG = "azure.keyvault.KeyVaultClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
            self, credentials, api_version=None, profile=KnownProfiles.default):
        super(ComputeManagementClient, self).__init__(
            credentials=credentials,
            api_version=api_version,
            profile=profile
        )

        self.config = KeyVaultClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

############ Generated from here ############

