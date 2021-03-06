import string
from uuid import uuid4

import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

from course_modes.helpers import CourseMode
from entitlements.models import CourseEntitlement, CourseEntitlementPolicy
from openedx.core.djangoapps.site_configuration.tests.factories import SiteFactory
from student.tests.factories import UserFactory


class CourseEntitlementPolicyFactory(factory.django.DjangoModelFactory):
    """
    Factory for a a CourseEntitlementPolicy
    """
    class Meta(object):
        model = CourseEntitlementPolicy

    site = factory.SubFactory(SiteFactory)


class CourseEntitlementFactory(factory.django.DjangoModelFactory):
    class Meta(object):
        model = CourseEntitlement

    uuid = factory.LazyFunction(uuid4)
    course_uuid = factory.LazyFunction(uuid4)
    mode = FuzzyChoice([CourseMode.VERIFIED, CourseMode.PROFESSIONAL])
    user = factory.SubFactory(UserFactory)
    order_number = FuzzyText(prefix='TEXTX', chars=string.digits)
    policy = factory.SubFactory(CourseEntitlementPolicyFactory)
