from django.test import TestCase
from django.core.urlresolvers import resolve
from EasyEquipment.views import home_page


class HomepageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
