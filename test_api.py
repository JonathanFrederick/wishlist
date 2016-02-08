from django.conf import settings
from requests import get, post, patch, delete as get, post, patch, delete
#
settings.configure()
ADDRESS = "localhost:8000/api/"


def smoke_test():
    """Test to make sure nosetests works"""
    assert True


def test_user_creation():
    """Testing ability to create a user with a call to the wishlist API"""
    response = post(ADDRESS+'user', data={'username': 'brother.bear',
                                          'first_name': 'Brother Bear',
                                          'last_name': 'Berenstain',
                                          'password': 'password',
                                          'email': 'bro.berenstain@gmail.com'})
    assert (response.status_code == 201)
