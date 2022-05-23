# coding: utf-8

"""
    Bumbal Client Api

    Bumbal API documentation  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: gerb@bumbal.eu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from bumbal.configuration import Configuration


class QuestionnaireQuestionOptionModel(object):
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
        'id': 'int',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text'
    }

    def __init__(self, id=None, text=None, _configuration=None):  # noqa: E501
        """QuestionnaireQuestionOptionModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._text = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text

    @property
    def id(self):
        """Gets the id of this QuestionnaireQuestionOptionModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this QuestionnaireQuestionOptionModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuestionnaireQuestionOptionModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this QuestionnaireQuestionOptionModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this QuestionnaireQuestionOptionModel.  # noqa: E501

        Option text  # noqa: E501

        :return: The text of this QuestionnaireQuestionOptionModel.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this QuestionnaireQuestionOptionModel.

        Option text  # noqa: E501

        :param text: The text of this QuestionnaireQuestionOptionModel.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(QuestionnaireQuestionOptionModel, dict):
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
        if not isinstance(other, QuestionnaireQuestionOptionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuestionnaireQuestionOptionModel):
            return True

        return self.to_dict() != other.to_dict()
