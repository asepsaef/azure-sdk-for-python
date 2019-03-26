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

from .resource import Resource


class InvoiceSummary(Resource):
    """An invoice resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar due_date: The due date for invoice.
    :vartype due_date: datetime
    :ivar invoice_date: The date when invoice was created.
    :vartype invoice_date: datetime
    :ivar status: Invoice status. Possible values include: 'PastDue', 'Due',
     'Paid', 'Void'
    :vartype status: str or ~azure.mgmt.billing.models.enum
    :ivar amount_due: Amount due.
    :vartype amount_due: ~azure.mgmt.billing.models.Amount
    :ivar billed_amount: Amount billed.
    :vartype billed_amount: ~azure.mgmt.billing.models.Amount
    :ivar invoice_period_start_date: The start date of the billing period.
    :vartype invoice_period_start_date: datetime
    :ivar invoice_period_end_date: The end date of the billing period.
    :vartype invoice_period_end_date: datetime
    :ivar billing_profile: The profile id which invoice belongs to.
    :vartype billing_profile: str
    :ivar billing_profile_name: The profile name which invoice belongs to.
    :vartype billing_profile_name: str
    :ivar purchase_order_number: The purchase identifier for the invoice.
    :vartype purchase_order_number: str
    :ivar document_urls: List of document urls available to download including
     invoice and tax documents.
    :vartype document_urls:
     list[~azure.mgmt.billing.models.DownloadProperties]
    :ivar payments: List of payments.
    :vartype payments: list[~azure.mgmt.billing.models.PaymentProperties]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'due_date': {'readonly': True},
        'invoice_date': {'readonly': True},
        'status': {'readonly': True},
        'amount_due': {'readonly': True},
        'billed_amount': {'readonly': True},
        'invoice_period_start_date': {'readonly': True},
        'invoice_period_end_date': {'readonly': True},
        'billing_profile': {'readonly': True},
        'billing_profile_name': {'readonly': True},
        'purchase_order_number': {'readonly': True},
        'document_urls': {'readonly': True},
        'payments': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'due_date': {'key': 'properties.dueDate', 'type': 'iso-8601'},
        'invoice_date': {'key': 'properties.invoiceDate', 'type': 'iso-8601'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'amount_due': {'key': 'properties.amountDue', 'type': 'Amount'},
        'billed_amount': {'key': 'properties.billedAmount', 'type': 'Amount'},
        'invoice_period_start_date': {'key': 'properties.invoicePeriodStartDate', 'type': 'iso-8601'},
        'invoice_period_end_date': {'key': 'properties.invoicePeriodEndDate', 'type': 'iso-8601'},
        'billing_profile': {'key': 'properties.billingProfile', 'type': 'str'},
        'billing_profile_name': {'key': 'properties.billingProfileName', 'type': 'str'},
        'purchase_order_number': {'key': 'properties.purchaseOrderNumber', 'type': 'str'},
        'document_urls': {'key': 'properties.documentUrls', 'type': '[DownloadProperties]'},
        'payments': {'key': 'properties.payments', 'type': '[PaymentProperties]'},
    }

    def __init__(self, **kwargs):
        super(InvoiceSummary, self).__init__(**kwargs)
        self.due_date = None
        self.invoice_date = None
        self.status = None
        self.amount_due = None
        self.billed_amount = None
        self.invoice_period_start_date = None
        self.invoice_period_end_date = None
        self.billing_profile = None
        self.billing_profile_name = None
        self.purchase_order_number = None
        self.document_urls = None
        self.payments = None
