# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.renewals_details_response_end_user_info import RenewalsDetailsResponseEndUserInfo

class TestRenewalsDetailsResponseEndUserInfo(unittest.TestCase):
    """RenewalsDetailsResponseEndUserInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenewalsDetailsResponseEndUserInfo:
        """Test RenewalsDetailsResponseEndUserInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenewalsDetailsResponseEndUserInfo`
        """
        model = RenewalsDetailsResponseEndUserInfo()
        if include_optional:
            return RenewalsDetailsResponseEndUserInfo(
                contact = '',
                name1 = '',
                name2 = '',
                company_name = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                address_line4 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                phone_number = '',
                email = ''
            )
        else:
            return RenewalsDetailsResponseEndUserInfo(
        )
        """

    def testRenewalsDetailsResponseEndUserInfo(self):
        """Test RenewalsDetailsResponseEndUserInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
