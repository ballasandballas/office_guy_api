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


class Body145(object):
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
        'subject': 'str',
        'contents_html': 'str',
        'contents_text': 'str',
        'ticket_type_id': 'int',
        'customer_id': 'int',
        'customer_email_address': 'str',
        'customer_name': 'str',
        'attachments': 'list[str]',
        'credentials': 'Object'
    }
    if hasattr(CustomerServiceTicketsCreateRequest, "swagger_types"):
        swagger_types.update(CustomerServiceTicketsCreateRequest.swagger_types)

    attribute_map = {
        'subject': 'Subject',
        'contents_html': 'ContentsHTML',
        'contents_text': 'ContentsText',
        'ticket_type_id': 'TicketTypeID',
        'customer_id': 'CustomerID',
        'customer_email_address': 'CustomerEmailAddress',
        'customer_name': 'CustomerName',
        'attachments': 'Attachments',
        'credentials': 'Credentials'
    }
    if hasattr(CustomerServiceTicketsCreateRequest, "attribute_map"):
        attribute_map.update(CustomerServiceTicketsCreateRequest.attribute_map)

    def __init__(self, subject=None, contents_html=None, contents_text=None, ticket_type_id=None, customer_id=None, customer_email_address=None, customer_name=None, attachments=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body145 - a model defined in Swagger"""  # noqa: E501
        self._subject = None
        self._contents_html = None
        self._contents_text = None
        self._ticket_type_id = None
        self._customer_id = None
        self._customer_email_address = None
        self._customer_name = None
        self._attachments = None
        self._credentials = None
        self.discriminator = None
        if subject is not None:
            self.subject = subject
        if contents_html is not None:
            self.contents_html = contents_html
        if contents_text is not None:
            self.contents_text = contents_text
        if ticket_type_id is not None:
            self.ticket_type_id = ticket_type_id
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_email_address is not None:
            self.customer_email_address = customer_email_address
        if customer_name is not None:
            self.customer_name = customer_name
        if attachments is not None:
            self.attachments = attachments
        self.credentials = credentials
        CustomerServiceTicketsCreateRequest.__init__(self, *args, **kwargs)

    @property
    def subject(self):
        """Gets the subject of this Body145.  # noqa: E501


        :return: The subject of this Body145.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Body145.


        :param subject: The subject of this Body145.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def contents_html(self):
        """Gets the contents_html of this Body145.  # noqa: E501


        :return: The contents_html of this Body145.  # noqa: E501
        :rtype: str
        """
        return self._contents_html

    @contents_html.setter
    def contents_html(self, contents_html):
        """Sets the contents_html of this Body145.


        :param contents_html: The contents_html of this Body145.  # noqa: E501
        :type: str
        """

        self._contents_html = contents_html

    @property
    def contents_text(self):
        """Gets the contents_text of this Body145.  # noqa: E501


        :return: The contents_text of this Body145.  # noqa: E501
        :rtype: str
        """
        return self._contents_text

    @contents_text.setter
    def contents_text(self, contents_text):
        """Sets the contents_text of this Body145.


        :param contents_text: The contents_text of this Body145.  # noqa: E501
        :type: str
        """

        self._contents_text = contents_text

    @property
    def ticket_type_id(self):
        """Gets the ticket_type_id of this Body145.  # noqa: E501


        :return: The ticket_type_id of this Body145.  # noqa: E501
        :rtype: int
        """
        return self._ticket_type_id

    @ticket_type_id.setter
    def ticket_type_id(self, ticket_type_id):
        """Sets the ticket_type_id of this Body145.


        :param ticket_type_id: The ticket_type_id of this Body145.  # noqa: E501
        :type: int
        """

        self._ticket_type_id = ticket_type_id

    @property
    def customer_id(self):
        """Gets the customer_id of this Body145.  # noqa: E501


        :return: The customer_id of this Body145.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Body145.


        :param customer_id: The customer_id of this Body145.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def customer_email_address(self):
        """Gets the customer_email_address of this Body145.  # noqa: E501


        :return: The customer_email_address of this Body145.  # noqa: E501
        :rtype: str
        """
        return self._customer_email_address

    @customer_email_address.setter
    def customer_email_address(self, customer_email_address):
        """Sets the customer_email_address of this Body145.


        :param customer_email_address: The customer_email_address of this Body145.  # noqa: E501
        :type: str
        """

        self._customer_email_address = customer_email_address

    @property
    def customer_name(self):
        """Gets the customer_name of this Body145.  # noqa: E501


        :return: The customer_name of this Body145.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this Body145.


        :param customer_name: The customer_name of this Body145.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def attachments(self):
        """Gets the attachments of this Body145.  # noqa: E501


        :return: The attachments of this Body145.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Body145.


        :param attachments: The attachments of this Body145.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def credentials(self):
        """Gets the credentials of this Body145.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body145.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body145.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body145.  # noqa: E501
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
        if issubclass(Body145, dict):
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
        if not isinstance(other, Body145):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
