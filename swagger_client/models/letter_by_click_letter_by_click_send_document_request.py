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


class LetterByClickLetterByClickSendDocumentRequest(object):
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
        'background_id': 'str',
        'recipient_address_line1': 'str',
        'recipient_address_line2': 'str',
        'recipient_address_line3': 'str',
        'recipient_city': 'str',
        'recipient_post_code': 'str',
        'recipient_title': 'str',
        'pdf': 'str',
        'sender_address': 'list[str]',
        'return_address': 'list[str]',
        'color': 'bool',
        'double_sided': 'bool',
        'mail_type': 'str',
        'live_mode': 'bool',
        'auto_rotate': 'bool',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'background_id': 'BackgroundID',
        'recipient_address_line1': 'RecipientAddressLine1',
        'recipient_address_line2': 'RecipientAddressLine2',
        'recipient_address_line3': 'RecipientAddressLine3',
        'recipient_city': 'RecipientCity',
        'recipient_post_code': 'RecipientPostCode',
        'recipient_title': 'RecipientTitle',
        'pdf': 'PDF',
        'sender_address': 'SenderAddress',
        'return_address': 'ReturnAddress',
        'color': 'Color',
        'double_sided': 'DoubleSided',
        'mail_type': 'MailType',
        'live_mode': 'LiveMode',
        'auto_rotate': 'AutoRotate',
        'credentials': 'Credentials'
    }

    def __init__(self, background_id=None, recipient_address_line1=None, recipient_address_line2=None, recipient_address_line3=None, recipient_city=None, recipient_post_code=None, recipient_title=None, pdf=None, sender_address=None, return_address=None, color=None, double_sided=None, mail_type=None, live_mode=None, auto_rotate=None, credentials=None):  # noqa: E501
        """LetterByClickLetterByClickSendDocumentRequest - a model defined in Swagger"""  # noqa: E501

        self._background_id = None
        self._recipient_address_line1 = None
        self._recipient_address_line2 = None
        self._recipient_address_line3 = None
        self._recipient_city = None
        self._recipient_post_code = None
        self._recipient_title = None
        self._pdf = None
        self._sender_address = None
        self._return_address = None
        self._color = None
        self._double_sided = None
        self._mail_type = None
        self._live_mode = None
        self._auto_rotate = None
        self._credentials = None
        self.discriminator = None

        if background_id is not None:
            self.background_id = background_id
        self.recipient_address_line1 = recipient_address_line1
        if recipient_address_line2 is not None:
            self.recipient_address_line2 = recipient_address_line2
        if recipient_address_line3 is not None:
            self.recipient_address_line3 = recipient_address_line3
        if recipient_city is not None:
            self.recipient_city = recipient_city
        if recipient_post_code is not None:
            self.recipient_post_code = recipient_post_code
        if recipient_title is not None:
            self.recipient_title = recipient_title
        self.pdf = pdf
        if sender_address is not None:
            self.sender_address = sender_address
        if return_address is not None:
            self.return_address = return_address
        if color is not None:
            self.color = color
        if double_sided is not None:
            self.double_sided = double_sided
        if mail_type is not None:
            self.mail_type = mail_type
        if live_mode is not None:
            self.live_mode = live_mode
        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        self.credentials = credentials

    @property
    def background_id(self):
        """Gets the background_id of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Template background ID<div><i>This field is supplied by Beeri  Defaults to the application settings.</i></div>  # noqa: E501

        :return: The background_id of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._background_id

    @background_id.setter
    def background_id(self, background_id):
        """Sets the background_id of this LetterByClickLetterByClickSendDocumentRequest.

        Template background ID<div><i>This field is supplied by Beeri  Defaults to the application settings.</i></div>  # noqa: E501

        :param background_id: The background_id of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """

        self._background_id = background_id

    @property
    def recipient_address_line1(self):
        """Gets the recipient_address_line1 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Recipient address line #1  # noqa: E501

        :return: The recipient_address_line1 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_address_line1

    @recipient_address_line1.setter
    def recipient_address_line1(self, recipient_address_line1):
        """Sets the recipient_address_line1 of this LetterByClickLetterByClickSendDocumentRequest.

        Recipient address line #1  # noqa: E501

        :param recipient_address_line1: The recipient_address_line1 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """
        if recipient_address_line1 is None:
            raise ValueError("Invalid value for `recipient_address_line1`, must not be `None`")  # noqa: E501

        self._recipient_address_line1 = recipient_address_line1

    @property
    def recipient_address_line2(self):
        """Gets the recipient_address_line2 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Recipient address line #2  # noqa: E501

        :return: The recipient_address_line2 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_address_line2

    @recipient_address_line2.setter
    def recipient_address_line2(self, recipient_address_line2):
        """Sets the recipient_address_line2 of this LetterByClickLetterByClickSendDocumentRequest.

        Recipient address line #2  # noqa: E501

        :param recipient_address_line2: The recipient_address_line2 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """

        self._recipient_address_line2 = recipient_address_line2

    @property
    def recipient_address_line3(self):
        """Gets the recipient_address_line3 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Recipient address line #3  # noqa: E501

        :return: The recipient_address_line3 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_address_line3

    @recipient_address_line3.setter
    def recipient_address_line3(self, recipient_address_line3):
        """Sets the recipient_address_line3 of this LetterByClickLetterByClickSendDocumentRequest.

        Recipient address line #3  # noqa: E501

        :param recipient_address_line3: The recipient_address_line3 of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """

        self._recipient_address_line3 = recipient_address_line3

    @property
    def recipient_city(self):
        """Gets the recipient_city of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Recipient city  # noqa: E501

        :return: The recipient_city of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_city

    @recipient_city.setter
    def recipient_city(self, recipient_city):
        """Sets the recipient_city of this LetterByClickLetterByClickSendDocumentRequest.

        Recipient city  # noqa: E501

        :param recipient_city: The recipient_city of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """

        self._recipient_city = recipient_city

    @property
    def recipient_post_code(self):
        """Gets the recipient_post_code of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Recipient post code (zipcode)  # noqa: E501

        :return: The recipient_post_code of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_post_code

    @recipient_post_code.setter
    def recipient_post_code(self, recipient_post_code):
        """Sets the recipient_post_code of this LetterByClickLetterByClickSendDocumentRequest.

        Recipient post code (zipcode)  # noqa: E501

        :param recipient_post_code: The recipient_post_code of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """

        self._recipient_post_code = recipient_post_code

    @property
    def recipient_title(self):
        """Gets the recipient_title of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Recipient title (name)  # noqa: E501

        :return: The recipient_title of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_title

    @recipient_title.setter
    def recipient_title(self, recipient_title):
        """Sets the recipient_title of this LetterByClickLetterByClickSendDocumentRequest.

        Recipient title (name)  # noqa: E501

        :param recipient_title: The recipient_title of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """

        self._recipient_title = recipient_title

    @property
    def pdf(self):
        """Gets the pdf of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        PDF file contents. Only A4 pages are supported.<div><i>Shouldn't be specified when using the SendMultipartDocument API method</i></div>  # noqa: E501

        :return: The pdf of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._pdf

    @pdf.setter
    def pdf(self, pdf):
        """Sets the pdf of this LetterByClickLetterByClickSendDocumentRequest.

        PDF file contents. Only A4 pages are supported.<div><i>Shouldn't be specified when using the SendMultipartDocument API method</i></div>  # noqa: E501

        :param pdf: The pdf of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """
        if pdf is None:
            raise ValueError("Invalid value for `pdf`, must not be `None`")  # noqa: E501
        if pdf is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', pdf):  # noqa: E501
            raise ValueError(r"Invalid value for `pdf`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._pdf = pdf

    @property
    def sender_address(self):
        """Gets the sender_address of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Specify up to 7 lines<div><i>Defaults to the application settings.</i></div>  # noqa: E501

        :return: The sender_address of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address):
        """Sets the sender_address of this LetterByClickLetterByClickSendDocumentRequest.

        Specify up to 7 lines<div><i>Defaults to the application settings.</i></div>  # noqa: E501

        :param sender_address: The sender_address of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: list[str]
        """

        self._sender_address = sender_address

    @property
    def return_address(self):
        """Gets the return_address of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Return address, specify up to 7 lines.<div><i>Defaults to the application settings.</i></div>  # noqa: E501

        :return: The return_address of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._return_address

    @return_address.setter
    def return_address(self, return_address):
        """Sets the return_address of this LetterByClickLetterByClickSendDocumentRequest.

        Return address, specify up to 7 lines.<div><i>Defaults to the application settings.</i></div>  # noqa: E501

        :param return_address: The return_address of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: list[str]
        """

        self._return_address = return_address

    @property
    def color(self):
        """Gets the color of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Indicates whether to print with Full Color (true) or black-white (false)<div><i>Defaults to Black-White (False)</i></div>  # noqa: E501

        :return: The color of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LetterByClickLetterByClickSendDocumentRequest.

        Indicates whether to print with Full Color (true) or black-white (false)<div><i>Defaults to Black-White (False)</i></div>  # noqa: E501

        :param color: The color of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: bool
        """

        self._color = color

    @property
    def double_sided(self):
        """Gets the double_sided of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Indicates whether to print on both page sides (true) or single-sided (false)<div><i>Defaults to Single-Sided (False)</i></div>  # noqa: E501

        :return: The double_sided of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._double_sided

    @double_sided.setter
    def double_sided(self, double_sided):
        """Sets the double_sided of this LetterByClickLetterByClickSendDocumentRequest.

        Indicates whether to print on both page sides (true) or single-sided (false)<div><i>Defaults to Single-Sided (False)</i></div>  # noqa: E501

        :param double_sided: The double_sided of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: bool
        """

        self._double_sided = double_sided

    @property
    def mail_type(self):
        """Gets the mail_type of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Mail type (Regular, Registered, Delivery Confirmation or Scanned Delivery Confirmation)<div><i>Defaults to Regular</i></div>  # noqa: E501

        :return: The mail_type of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._mail_type

    @mail_type.setter
    def mail_type(self, mail_type):
        """Sets the mail_type of this LetterByClickLetterByClickSendDocumentRequest.

        Mail type (Regular, Registered, Delivery Confirmation or Scanned Delivery Confirmation)<div><i>Defaults to Regular</i></div>  # noqa: E501

        :param mail_type: The mail_type of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Regular", "Registered", "DeliveryConfirmation", "ScannedDeliveryConfirmation"]  # noqa: E501
        if mail_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mail_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mail_type, allowed_values)
            )

        self._mail_type = mail_type

    @property
    def live_mode(self):
        """Gets the live_mode of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Indicated whether this is a live or a test API call.<div><i>Defaults to test (False)</i></div>  # noqa: E501

        :return: The live_mode of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._live_mode

    @live_mode.setter
    def live_mode(self, live_mode):
        """Sets the live_mode of this LetterByClickLetterByClickSendDocumentRequest.

        Indicated whether this is a live or a test API call.<div><i>Defaults to test (False)</i></div>  # noqa: E501

        :param live_mode: The live_mode of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: bool
        """

        self._live_mode = live_mode

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Indicated whether to auto rotate the document to portrait if needed.  Please note this incurs performance hit, and should only be used when necessary.<div><i>Defaults to False</i></div>  # noqa: E501

        :return: The auto_rotate of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this LetterByClickLetterByClickSendDocumentRequest.

        Indicated whether to auto rotate the document to portrait if needed.  Please note this incurs performance hit, and should only be used when necessary.<div><i>Defaults to False</i></div>  # noqa: E501

        :param auto_rotate: The auto_rotate of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :type: bool
        """

        self._auto_rotate = auto_rotate

    @property
    def credentials(self):
        """Gets the credentials of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this LetterByClickLetterByClickSendDocumentRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this LetterByClickLetterByClickSendDocumentRequest.  # noqa: E501
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
        if issubclass(LetterByClickLetterByClickSendDocumentRequest, dict):
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
        if not isinstance(other, LetterByClickLetterByClickSendDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
