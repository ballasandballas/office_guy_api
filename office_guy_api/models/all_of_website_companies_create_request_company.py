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


class AllOfWebsiteCompaniesCreateRequestCompany(object):
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
        'name': 'str',
        'email_address': 'str',
        'country': 'str',
        'address': 'str',
        'phone': 'str',
        'fax': 'str',
        'title': 'str',
        'corporate_number': 'str',
        'english_name': 'str',
        'english_address': 'str',
        'english_country': 'str',
        'english_phone': 'str',
        'english_fax': 'str',
        'english_title': 'str',
        'company_type': 'Object',
        'logo': 'str',
        'website': 'str'
    }
    if hasattr(WebsiteTypedCompany, "swagger_types"):
        swagger_types.update(WebsiteTypedCompany.swagger_types)

    attribute_map = {
        'name': 'Name',
        'email_address': 'EmailAddress',
        'country': 'Country',
        'address': 'Address',
        'phone': 'Phone',
        'fax': 'Fax',
        'title': 'Title',
        'corporate_number': 'CorporateNumber',
        'english_name': 'English_Name',
        'english_address': 'English_Address',
        'english_country': 'English_Country',
        'english_phone': 'English_Phone',
        'english_fax': 'English_Fax',
        'english_title': 'English_Title',
        'company_type': 'CompanyType',
        'logo': 'Logo',
        'website': 'Website'
    }
    if hasattr(WebsiteTypedCompany, "attribute_map"):
        attribute_map.update(WebsiteTypedCompany.attribute_map)

    def __init__(self, name=None, email_address=None, country=None, address=None, phone=None, fax=None, title=None, corporate_number=None, english_name=None, english_address=None, english_country=None, english_phone=None, english_fax=None, english_title=None, company_type=None, logo=None, website=None, *args, **kwargs):  # noqa: E501
        """AllOfWebsiteCompaniesCreateRequestCompany - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._email_address = None
        self._country = None
        self._address = None
        self._phone = None
        self._fax = None
        self._title = None
        self._corporate_number = None
        self._english_name = None
        self._english_address = None
        self._english_country = None
        self._english_phone = None
        self._english_fax = None
        self._english_title = None
        self._company_type = None
        self._logo = None
        self._website = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if email_address is not None:
            self.email_address = email_address
        if country is not None:
            self.country = country
        if address is not None:
            self.address = address
        if phone is not None:
            self.phone = phone
        if fax is not None:
            self.fax = fax
        if title is not None:
            self.title = title
        if corporate_number is not None:
            self.corporate_number = corporate_number
        if english_name is not None:
            self.english_name = english_name
        if english_address is not None:
            self.english_address = english_address
        if english_country is not None:
            self.english_country = english_country
        if english_phone is not None:
            self.english_phone = english_phone
        if english_fax is not None:
            self.english_fax = english_fax
        if english_title is not None:
            self.english_title = english_title
        if company_type is not None:
            self.company_type = company_type
        if logo is not None:
            self.logo = logo
        if website is not None:
            self.website = website
        WebsiteTypedCompany.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization name  # noqa: E501

        :return: The name of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization name  # noqa: E501

        :param name: The name of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email_address(self):
        """Gets the email_address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization email address<div><i>Optional field</i></div>  # noqa: E501

        :return: The email_address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization email address<div><i>Optional field</i></div>  # noqa: E501

        :param email_address: The email_address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def country(self):
        """Gets the country of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization country<div><i>Optional field</i></div>  # noqa: E501

        :return: The country of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization country<div><i>Optional field</i></div>  # noqa: E501

        :param country: The country of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def address(self):
        """Gets the address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization address<div><i>Optional field</i></div>  # noqa: E501

        :return: The address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization address<div><i>Optional field</i></div>  # noqa: E501

        :param address: The address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def phone(self):
        """Gets the phone of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization phone number<div><i>Optional field</i></div>  # noqa: E501

        :return: The phone of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization phone number<div><i>Optional field</i></div>  # noqa: E501

        :param phone: The phone of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """Gets the fax of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization fax number<div><i>Optional field</i></div>  # noqa: E501

        :return: The fax of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization fax number<div><i>Optional field</i></div>  # noqa: E501

        :param fax: The fax of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def title(self):
        """Gets the title of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization title<div><i>Optional field</i></div>  # noqa: E501

        :return: The title of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization title<div><i>Optional field</i></div>  # noqa: E501

        :param title: The title of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def corporate_number(self):
        """Gets the corporate_number of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization TAX identifier<div><i>Optional field</i></div>  # noqa: E501

        :return: The corporate_number of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._corporate_number

    @corporate_number.setter
    def corporate_number(self, corporate_number):
        """Sets the corporate_number of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization TAX identifier<div><i>Optional field</i></div>  # noqa: E501

        :param corporate_number: The corporate_number of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._corporate_number = corporate_number

    @property
    def english_name(self):
        """Gets the english_name of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        English organization name<div><i>Optional field</i></div>  # noqa: E501

        :return: The english_name of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this AllOfWebsiteCompaniesCreateRequestCompany.

        English organization name<div><i>Optional field</i></div>  # noqa: E501

        :param english_name: The english_name of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._english_name = english_name

    @property
    def english_address(self):
        """Gets the english_address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        English organization address<div><i>Optional field</i></div>  # noqa: E501

        :return: The english_address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._english_address

    @english_address.setter
    def english_address(self, english_address):
        """Sets the english_address of this AllOfWebsiteCompaniesCreateRequestCompany.

        English organization address<div><i>Optional field</i></div>  # noqa: E501

        :param english_address: The english_address of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._english_address = english_address

    @property
    def english_country(self):
        """Gets the english_country of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        English organization country<div><i>Optional field</i></div>  # noqa: E501

        :return: The english_country of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._english_country

    @english_country.setter
    def english_country(self, english_country):
        """Sets the english_country of this AllOfWebsiteCompaniesCreateRequestCompany.

        English organization country<div><i>Optional field</i></div>  # noqa: E501

        :param english_country: The english_country of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._english_country = english_country

    @property
    def english_phone(self):
        """Gets the english_phone of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        English organization phone<div><i>Optional field</i></div>  # noqa: E501

        :return: The english_phone of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._english_phone

    @english_phone.setter
    def english_phone(self, english_phone):
        """Sets the english_phone of this AllOfWebsiteCompaniesCreateRequestCompany.

        English organization phone<div><i>Optional field</i></div>  # noqa: E501

        :param english_phone: The english_phone of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._english_phone = english_phone

    @property
    def english_fax(self):
        """Gets the english_fax of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        English organization fax number<div><i>Optional field</i></div>  # noqa: E501

        :return: The english_fax of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._english_fax

    @english_fax.setter
    def english_fax(self, english_fax):
        """Sets the english_fax of this AllOfWebsiteCompaniesCreateRequestCompany.

        English organization fax number<div><i>Optional field</i></div>  # noqa: E501

        :param english_fax: The english_fax of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._english_fax = english_fax

    @property
    def english_title(self):
        """Gets the english_title of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        English organization title  # noqa: E501

        :return: The english_title of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._english_title

    @english_title.setter
    def english_title(self, english_title):
        """Sets the english_title of this AllOfWebsiteCompaniesCreateRequestCompany.

        English organization title  # noqa: E501

        :param english_title: The english_title of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._english_title = english_title

    @property
    def company_type(self):
        """Gets the company_type of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Organization type<div><i>CompanyWithVAT - חברה  VATExemptDealer - עמותה  LicensedDealer - עוסק מורשה  Fellowship - עמותה  Partnership - שותפות  CommunityInterestCompany - חברה לתועלת הציבור  Cooperative - אגודה שיתופית  HouseCommittee - ועד בית  ElectionGroup - סיעה לבחירות  Party - מפלגה</i></div>  # noqa: E501

        :return: The company_type of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: Object
        """
        return self._company_type

    @company_type.setter
    def company_type(self, company_type):
        """Sets the company_type of this AllOfWebsiteCompaniesCreateRequestCompany.

        Organization type<div><i>CompanyWithVAT - חברה  VATExemptDealer - עמותה  LicensedDealer - עוסק מורשה  Fellowship - עמותה  Partnership - שותפות  CommunityInterestCompany - חברה לתועלת הציבור  Cooperative - אגודה שיתופית  HouseCommittee - ועד בית  ElectionGroup - סיעה לבחירות  Party - מפלגה</i></div>  # noqa: E501

        :param company_type: The company_type of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: Object
        """

        self._company_type = company_type

    @property
    def logo(self):
        """Gets the logo of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Logo image file<div><i>File should be a standard PNG/JPG/GIF file</i></div>  # noqa: E501

        :return: The logo of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this AllOfWebsiteCompaniesCreateRequestCompany.

        Logo image file<div><i>File should be a standard PNG/JPG/GIF file</i></div>  # noqa: E501

        :param logo: The logo of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def website(self):
        """Gets the website of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501

        Website URL  # noqa: E501

        :return: The website of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this AllOfWebsiteCompaniesCreateRequestCompany.

        Website URL  # noqa: E501

        :param website: The website of this AllOfWebsiteCompaniesCreateRequestCompany.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(AllOfWebsiteCompaniesCreateRequestCompany, dict):
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
        if not isinstance(other, AllOfWebsiteCompaniesCreateRequestCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
