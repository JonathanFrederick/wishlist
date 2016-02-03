from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class UserTestCase(TestCase):
    # Entire user story will go here
    def setUp(self):
        test_user = User.objects.create(
            username="brother.bear",
            password="password",
            first_name="Brother Bear",
            last_name="Berenstain",
        )

    # Checks that users are being created in the database
    def test_user_creation(self):
        self.assertEquals(User.objects.get(username='brother.bear').first_name, 'Brother Bear')
        self.assertEquals(User.objects.get(username='brother.bear').last_name, 'Berenstain')
