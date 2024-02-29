# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.availability_async_notification_request_resource_inner_links_inner import AvailabilityAsyncNotificationRequestResourceInnerLinksInner

class TestAvailabilityAsyncNotificationRequestResourceInnerLinksInner(unittest.TestCase):
    """AvailabilityAsyncNotificationRequestResourceInnerLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvailabilityAsyncNotificationRequestResourceInnerLinksInner:
        """Test AvailabilityAsyncNotificationRequestResourceInnerLinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvailabilityAsyncNotificationRequestResourceInnerLinksInner`
        """
        model = AvailabilityAsyncNotificationRequestResourceInnerLinksInner()
        if include_optional:
            return AvailabilityAsyncNotificationRequestResourceInnerLinksInner(
                topic = '',
                href = '',
                type = ''
            )
        else:
            return AvailabilityAsyncNotificationRequestResourceInnerLinksInner(
        )
        """

    def testAvailabilityAsyncNotificationRequestResourceInnerLinksInner(self):
        """Test AvailabilityAsyncNotificationRequestResourceInnerLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
