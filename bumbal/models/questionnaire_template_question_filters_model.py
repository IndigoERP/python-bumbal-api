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


class QuestionnaireTemplateQuestionFiltersModel(object):
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
        'id': 'list[int]',
        'search_text': 'str',
        'updated_at_since': 'datetime',
        'updated_at_till': 'datetime',
        'question_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'search_text': 'search_text',
        'updated_at_since': 'updated_at_since',
        'updated_at_till': 'updated_at_till',
        'question_type': 'question_type'
    }

    def __init__(self, id=None, search_text=None, updated_at_since=None, updated_at_till=None, question_type=None, _configuration=None):  # noqa: E501
        """QuestionnaireTemplateQuestionFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._search_text = None
        self._updated_at_since = None
        self._updated_at_till = None
        self._question_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if search_text is not None:
            self.search_text = search_text
        if updated_at_since is not None:
            self.updated_at_since = updated_at_since
        if updated_at_till is not None:
            self.updated_at_till = updated_at_till
        if question_type is not None:
            self.question_type = question_type

    @property
    def id(self):
        """Gets the id of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501

        QuestionnaireTemplateQuestion id's  # noqa: E501

        :return: The id of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuestionnaireTemplateQuestionFiltersModel.

        QuestionnaireTemplateQuestion id's  # noqa: E501

        :param id: The id of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._id = id

    @property
    def search_text(self):
        """Gets the search_text of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501

        free search through text and numeric type columns  # noqa: E501

        :return: The search_text of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this QuestionnaireTemplateQuestionFiltersModel.

        free search through text and numeric type columns  # noqa: E501

        :param search_text: The search_text of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def updated_at_since(self):
        """Gets the updated_at_since of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501

        Show updated since  # noqa: E501

        :return: The updated_at_since of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_since

    @updated_at_since.setter
    def updated_at_since(self, updated_at_since):
        """Sets the updated_at_since of this QuestionnaireTemplateQuestionFiltersModel.

        Show updated since  # noqa: E501

        :param updated_at_since: The updated_at_since of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_since = updated_at_since

    @property
    def updated_at_till(self):
        """Gets the updated_at_till of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501

        Show updated till  # noqa: E501

        :return: The updated_at_till of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_till

    @updated_at_till.setter
    def updated_at_till(self, updated_at_till):
        """Sets the updated_at_till of this QuestionnaireTemplateQuestionFiltersModel.

        Show updated till  # noqa: E501

        :param updated_at_till: The updated_at_till of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_till = updated_at_till

    @property
    def question_type(self):
        """Gets the question_type of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501

        Question Type  # noqa: E501

        :return: The question_type of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :rtype: str
        """
        return self._question_type

    @question_type.setter
    def question_type(self, question_type):
        """Sets the question_type of this QuestionnaireTemplateQuestionFiltersModel.

        Question Type  # noqa: E501

        :param question_type: The question_type of this QuestionnaireTemplateQuestionFiltersModel.  # noqa: E501
        :type: str
        """

        self._question_type = question_type

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
        if issubclass(QuestionnaireTemplateQuestionFiltersModel, dict):
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
        if not isinstance(other, QuestionnaireTemplateQuestionFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuestionnaireTemplateQuestionFiltersModel):
            return True

        return self.to_dict() != other.to_dict()
