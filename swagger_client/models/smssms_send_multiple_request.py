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


class SMSSMSSendMultipleRequest(object):
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
        'recipients': 'list[str]',
        'text': 'str',
        'save_draft': 'bool',
        'schedule': 'datetime',
        'sender': 'str',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'recipients': 'Recipients',
        'text': 'Text',
        'save_draft': 'SaveDraft',
        'schedule': 'Schedule',
        'sender': 'Sender',
        'credentials': 'Credentials'
    }

    def __init__(self, recipients=None, text=None, save_draft=None, schedule=None, sender=None, credentials=None):  # noqa: E501
        """SMSSMSSendMultipleRequest - a model defined in Swagger"""  # noqa: E501

        self._recipients = None
        self._text = None
        self._save_draft = None
        self._schedule = None
        self._sender = None
        self._credentials = None
        self.discriminator = None

        self.recipients = recipients
        self.text = text
        if save_draft is not None:
            self.save_draft = save_draft
        if schedule is not None:
            self.schedule = schedule
        if sender is not None:
            self.sender = sender
        self.credentials = credentials

    @property
    def recipients(self):
        """Gets the recipients of this SMSSMSSendMultipleRequest.  # noqa: E501

        Recipients  # noqa: E501

        :return: The recipients of this SMSSMSSendMultipleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this SMSSMSSendMultipleRequest.

        Recipients  # noqa: E501

        :param recipients: The recipients of this SMSSMSSendMultipleRequest.  # noqa: E501
        :type: list[str]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def text(self):
        """Gets the text of this SMSSMSSendMultipleRequest.  # noqa: E501

        Body (formatted as HTML)  # noqa: E501

        :return: The text of this SMSSMSSendMultipleRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SMSSMSSendMultipleRequest.

        Body (formatted as HTML)  # noqa: E501

        :param text: The text of this SMSSMSSendMultipleRequest.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def save_draft(self):
        """Gets the save_draft of this SMSSMSSendMultipleRequest.  # noqa: E501

        Save as draft? (Prevents automatic sending)<div><i>Defaults to false (No draft)</i></div>  # noqa: E501

        :return: The save_draft of this SMSSMSSendMultipleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._save_draft

    @save_draft.setter
    def save_draft(self, save_draft):
        """Sets the save_draft of this SMSSMSSendMultipleRequest.

        Save as draft? (Prevents automatic sending)<div><i>Defaults to false (No draft)</i></div>  # noqa: E501

        :param save_draft: The save_draft of this SMSSMSSendMultipleRequest.  # noqa: E501
        :type: bool
        """

        self._save_draft = save_draft

    @property
    def schedule(self):
        """Gets the schedule of this SMSSMSSendMultipleRequest.  # noqa: E501

        Schedule sending for a future date<div><i>Not supported for draft saving</i></div>  # noqa: E501

        :return: The schedule of this SMSSMSSendMultipleRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SMSSMSSendMultipleRequest.

        Schedule sending for a future date<div><i>Not supported for draft saving</i></div>  # noqa: E501

        :param schedule: The schedule of this SMSSMSSendMultipleRequest.  # noqa: E501
        :type: datetime
        """

        self._schedule = schedule

    @property
    def sender(self):
        """Gets the sender of this SMSSMSSendMultipleRequest.  # noqa: E501

        Sender number<div><i>Sender number should be verified prior to sending SMS messages</i></div>  # noqa: E501

        :return: The sender of this SMSSMSSendMultipleRequest.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SMSSMSSendMultipleRequest.

        Sender number<div><i>Sender number should be verified prior to sending SMS messages</i></div>  # noqa: E501

        :param sender: The sender of this SMSSMSSendMultipleRequest.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def credentials(self):
        """Gets the credentials of this SMSSMSSendMultipleRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this SMSSMSSendMultipleRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this SMSSMSSendMultipleRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this SMSSMSSendMultipleRequest.  # noqa: E501
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
        if issubclass(SMSSMSSendMultipleRequest, dict):
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
        if not isinstance(other, SMSSMSSendMultipleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
