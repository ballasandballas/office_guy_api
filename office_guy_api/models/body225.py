# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-06-20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body225(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'automatic_billing': 'bool',
        'automatic_billing_credit_card': 'bool',
        'automatic_billing_direct_debit': 'bool',
        'automatic_billing_documents_only': 'bool',
        'automatic_billing_proforma_invoices': 'bool',
        'automatic_billing_payment_requests': 'bool',
        'automatic_billing_invoices': 'bool',
        'automatic_billing_charge_document': 'Object',
        'automatic_billing_documents_only_document': 'Object',
        'credentials': 'Object'
    }
    if hasattr(BillingRecurringUpdateSettingsRequest, "swagger_types"):
        swagger_types.update(BillingRecurringUpdateSettingsRequest.swagger_types)

    attribute_map = {
        'automatic_billing': 'AutomaticBilling',
        'automatic_billing_credit_card': 'AutomaticBilling_CreditCard',
        'automatic_billing_direct_debit': 'AutomaticBilling_DirectDebit',
        'automatic_billing_documents_only': 'AutomaticBilling_DocumentsOnly',
        'automatic_billing_proforma_invoices': 'AutomaticBilling_ProformaInvoices',
        'automatic_billing_payment_requests': 'AutomaticBilling_PaymentRequests',
        'automatic_billing_invoices': 'AutomaticBilling_Invoices',
        'automatic_billing_charge_document': 'AutomaticBilling_ChargeDocument',
        'automatic_billing_documents_only_document': 'AutomaticBilling_DocumentsOnlyDocument',
        'credentials': 'Credentials'
    }
    if hasattr(BillingRecurringUpdateSettingsRequest, "attribute_map"):
        attribute_map.update(BillingRecurringUpdateSettingsRequest.attribute_map)

    def __init__(self, automatic_billing=None, automatic_billing_credit_card=None, automatic_billing_direct_debit=None, automatic_billing_documents_only=None, automatic_billing_proforma_invoices=None, automatic_billing_payment_requests=None, automatic_billing_invoices=None, automatic_billing_charge_document=None, automatic_billing_documents_only_document=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body225 - a model defined in Swagger"""  # noqa: E501
        self._automatic_billing = None
        self._automatic_billing_credit_card = None
        self._automatic_billing_direct_debit = None
        self._automatic_billing_documents_only = None
        self._automatic_billing_proforma_invoices = None
        self._automatic_billing_payment_requests = None
        self._automatic_billing_invoices = None
        self._automatic_billing_charge_document = None
        self._automatic_billing_documents_only_document = None
        self._credentials = None
        self.discriminator = None
        if automatic_billing is not None:
            self.automatic_billing = automatic_billing
        if automatic_billing_credit_card is not None:
            self.automatic_billing_credit_card = automatic_billing_credit_card
        if automatic_billing_direct_debit is not None:
            self.automatic_billing_direct_debit = automatic_billing_direct_debit
        if automatic_billing_documents_only is not None:
            self.automatic_billing_documents_only = automatic_billing_documents_only
        if automatic_billing_proforma_invoices is not None:
            self.automatic_billing_proforma_invoices = automatic_billing_proforma_invoices
        if automatic_billing_payment_requests is not None:
            self.automatic_billing_payment_requests = automatic_billing_payment_requests
        if automatic_billing_invoices is not None:
            self.automatic_billing_invoices = automatic_billing_invoices
        if automatic_billing_charge_document is not None:
            self.automatic_billing_charge_document = automatic_billing_charge_document
        if automatic_billing_documents_only_document is not None:
            self.automatic_billing_documents_only_document = automatic_billing_documents_only_document
        self.credentials = credentials
        BillingRecurringUpdateSettingsRequest.__init__(self, *args, **kwargs)

    @property
    def automatic_billing(self):
        """Gets the automatic_billing of this Body225.  # noqa: E501

        Automatic billing mode  # noqa: E501

        :return: The automatic_billing of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing

    @automatic_billing.setter
    def automatic_billing(self, automatic_billing):
        """Sets the automatic_billing of this Body225.

        Automatic billing mode  # noqa: E501

        :param automatic_billing: The automatic_billing of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing = automatic_billing

    @property
    def automatic_billing_credit_card(self):
        """Gets the automatic_billing_credit_card of this Body225.  # noqa: E501

        Automatic billing mode for credit card payments  # noqa: E501

        :return: The automatic_billing_credit_card of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing_credit_card

    @automatic_billing_credit_card.setter
    def automatic_billing_credit_card(self, automatic_billing_credit_card):
        """Sets the automatic_billing_credit_card of this Body225.

        Automatic billing mode for credit card payments  # noqa: E501

        :param automatic_billing_credit_card: The automatic_billing_credit_card of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing_credit_card = automatic_billing_credit_card

    @property
    def automatic_billing_direct_debit(self):
        """Gets the automatic_billing_direct_debit of this Body225.  # noqa: E501

        Automatic billing mode for direct debit payments  # noqa: E501

        :return: The automatic_billing_direct_debit of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing_direct_debit

    @automatic_billing_direct_debit.setter
    def automatic_billing_direct_debit(self, automatic_billing_direct_debit):
        """Sets the automatic_billing_direct_debit of this Body225.

        Automatic billing mode for direct debit payments  # noqa: E501

        :param automatic_billing_direct_debit: The automatic_billing_direct_debit of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing_direct_debit = automatic_billing_direct_debit

    @property
    def automatic_billing_documents_only(self):
        """Gets the automatic_billing_documents_only of this Body225.  # noqa: E501

        Automatic billing mode for documents only  # noqa: E501

        :return: The automatic_billing_documents_only of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing_documents_only

    @automatic_billing_documents_only.setter
    def automatic_billing_documents_only(self, automatic_billing_documents_only):
        """Sets the automatic_billing_documents_only of this Body225.

        Automatic billing mode for documents only  # noqa: E501

        :param automatic_billing_documents_only: The automatic_billing_documents_only of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing_documents_only = automatic_billing_documents_only

    @property
    def automatic_billing_proforma_invoices(self):
        """Gets the automatic_billing_proforma_invoices of this Body225.  # noqa: E501

        Automatic billing mode for charging existing proforma invoices  # noqa: E501

        :return: The automatic_billing_proforma_invoices of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing_proforma_invoices

    @automatic_billing_proforma_invoices.setter
    def automatic_billing_proforma_invoices(self, automatic_billing_proforma_invoices):
        """Sets the automatic_billing_proforma_invoices of this Body225.

        Automatic billing mode for charging existing proforma invoices  # noqa: E501

        :param automatic_billing_proforma_invoices: The automatic_billing_proforma_invoices of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing_proforma_invoices = automatic_billing_proforma_invoices

    @property
    def automatic_billing_payment_requests(self):
        """Gets the automatic_billing_payment_requests of this Body225.  # noqa: E501

        Automatic billing mode for charging existing payment requests  # noqa: E501

        :return: The automatic_billing_payment_requests of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing_payment_requests

    @automatic_billing_payment_requests.setter
    def automatic_billing_payment_requests(self, automatic_billing_payment_requests):
        """Sets the automatic_billing_payment_requests of this Body225.

        Automatic billing mode for charging existing payment requests  # noqa: E501

        :param automatic_billing_payment_requests: The automatic_billing_payment_requests of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing_payment_requests = automatic_billing_payment_requests

    @property
    def automatic_billing_invoices(self):
        """Gets the automatic_billing_invoices of this Body225.  # noqa: E501

        Automatic billing mode charging existing tax invoices  # noqa: E501

        :return: The automatic_billing_invoices of this Body225.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_billing_invoices

    @automatic_billing_invoices.setter
    def automatic_billing_invoices(self, automatic_billing_invoices):
        """Sets the automatic_billing_invoices of this Body225.

        Automatic billing mode charging existing tax invoices  # noqa: E501

        :param automatic_billing_invoices: The automatic_billing_invoices of this Body225.  # noqa: E501
        :type: bool
        """

        self._automatic_billing_invoices = automatic_billing_invoices

    @property
    def automatic_billing_charge_document(self):
        """Gets the automatic_billing_charge_document of this Body225.  # noqa: E501

        Default document type for charges billing  # noqa: E501

        :return: The automatic_billing_charge_document of this Body225.  # noqa: E501
        :rtype: Object
        """
        return self._automatic_billing_charge_document

    @automatic_billing_charge_document.setter
    def automatic_billing_charge_document(self, automatic_billing_charge_document):
        """Sets the automatic_billing_charge_document of this Body225.

        Default document type for charges billing  # noqa: E501

        :param automatic_billing_charge_document: The automatic_billing_charge_document of this Body225.  # noqa: E501
        :type: Object
        """

        self._automatic_billing_charge_document = automatic_billing_charge_document

    @property
    def automatic_billing_documents_only_document(self):
        """Gets the automatic_billing_documents_only_document of this Body225.  # noqa: E501

        Default document type for documents only billing  # noqa: E501

        :return: The automatic_billing_documents_only_document of this Body225.  # noqa: E501
        :rtype: Object
        """
        return self._automatic_billing_documents_only_document

    @automatic_billing_documents_only_document.setter
    def automatic_billing_documents_only_document(self, automatic_billing_documents_only_document):
        """Sets the automatic_billing_documents_only_document of this Body225.

        Default document type for documents only billing  # noqa: E501

        :param automatic_billing_documents_only_document: The automatic_billing_documents_only_document of this Body225.  # noqa: E501
        :type: Object
        """

        self._automatic_billing_documents_only_document = automatic_billing_documents_only_document

    @property
    def credentials(self):
        """Gets the credentials of this Body225.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body225.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body225.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body225.  # noqa: E501
        :type: Object
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body225, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body225):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
