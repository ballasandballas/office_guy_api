# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountingGeneralVerifyBankAccountRequest(object):
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
        'bank_code': 'int',
        'branch_code': 'int',
        'account_number': 'int',
        'verify_branch_number': 'bool',
        'verify_limited_account': 'bool',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'bank_code': 'BankCode',
        'branch_code': 'BranchCode',
        'account_number': 'AccountNumber',
        'verify_branch_number': 'VerifyBranchNumber',
        'verify_limited_account': 'VerifyLimitedAccount',
        'credentials': 'Credentials'
    }

    def __init__(self, bank_code=None, branch_code=None, account_number=None, verify_branch_number=None, verify_limited_account=None, credentials=None):  # noqa: E501
        """AccountingGeneralVerifyBankAccountRequest - a model defined in Swagger"""  # noqa: E501

        self._bank_code = None
        self._branch_code = None
        self._account_number = None
        self._verify_branch_number = None
        self._verify_limited_account = None
        self._credentials = None
        self.discriminator = None

        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        if verify_branch_number is not None:
            self.verify_branch_number = verify_branch_number
        if verify_limited_account is not None:
            self.verify_limited_account = verify_limited_account
        self.credentials = credentials

    @property
    def bank_code(self):
        """Gets the bank_code of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501

        Bank code  # noqa: E501

        :return: The bank_code of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this AccountingGeneralVerifyBankAccountRequest.

        Bank code  # noqa: E501

        :param bank_code: The bank_code of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :type: int
        """
        if bank_code is None:
            raise ValueError("Invalid value for `bank_code`, must not be `None`")  # noqa: E501

        self._bank_code = bank_code

    @property
    def branch_code(self):
        """Gets the branch_code of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501

        Branch code  # noqa: E501

        :return: The branch_code of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this AccountingGeneralVerifyBankAccountRequest.

        Branch code  # noqa: E501

        :param branch_code: The branch_code of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :type: int
        """
        if branch_code is None:
            raise ValueError("Invalid value for `branch_code`, must not be `None`")  # noqa: E501

        self._branch_code = branch_code

    @property
    def account_number(self):
        """Gets the account_number of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501

        Account number  # noqa: E501

        :return: The account_number of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AccountingGeneralVerifyBankAccountRequest.

        Account number  # noqa: E501

        :param account_number: The account_number of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :type: int
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def verify_branch_number(self):
        """Gets the verify_branch_number of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501

        Verifies if the branch exists  # noqa: E501

        :return: The verify_branch_number of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._verify_branch_number

    @verify_branch_number.setter
    def verify_branch_number(self, verify_branch_number):
        """Sets the verify_branch_number of this AccountingGeneralVerifyBankAccountRequest.

        Verifies if the branch exists  # noqa: E501

        :param verify_branch_number: The verify_branch_number of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :type: bool
        """

        self._verify_branch_number = verify_branch_number

    @property
    def verify_limited_account(self):
        """Gets the verify_limited_account of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501

        Verifies if the account is limited in addition  # noqa: E501

        :return: The verify_limited_account of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._verify_limited_account

    @verify_limited_account.setter
    def verify_limited_account(self, verify_limited_account):
        """Sets the verify_limited_account of this AccountingGeneralVerifyBankAccountRequest.

        Verifies if the account is limited in addition  # noqa: E501

        :param verify_limited_account: The verify_limited_account of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :type: bool
        """

        self._verify_limited_account = verify_limited_account

    @property
    def credentials(self):
        """Gets the credentials of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AccountingGeneralVerifyBankAccountRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this AccountingGeneralVerifyBankAccountRequest.  # noqa: E501
        :type: CoreAPICredentials
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
        if issubclass(AccountingGeneralVerifyBankAccountRequest, dict):
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
        if not isinstance(other, AccountingGeneralVerifyBankAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
