from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')


# test that Django server can run
assert 'Django' in browser.title
