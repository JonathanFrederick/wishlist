from selenium import webdriver
# from django.conf import settings

# settings.configure()

# for local testing
ADDRESS = 'http://localhost:8000'

# for remote testing
# ADDRESS = TBD


def smoke_test():
    """Test to make sure nosetests works"""
    assert True


def test_django_running():
    """Test that Django server can run"""
    browser = webdriver.Firefox()
    browser.get(ADDRESS)
    assert 'Django' in browser.title
