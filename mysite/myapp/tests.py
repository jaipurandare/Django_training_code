from django.test import TestCase
from myapp.models import Role
# Create your tests here.

class RoleTestCase(TestCase):
    def setUp(self):
        Role.objects.create(name="Manager")

    def test_role_fancy_name_format(self):
        """Fancy name for Role is fomated correctly with 3 exclaimation marks"""
        manager_role = Role.objects.get(name="Manager")
        self.assertEqual(manager_role.fancy_name(), 'Manager!!!')