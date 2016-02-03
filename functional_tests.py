from selenium import webdriver


# for local testing
ADDRESS = 'http://localhost:8000'

# for remote testing
# ADDRESS = TBD

browser = webdriver.Firefox()
browser.get(ADDRESS)


# test that Django server can run
assert 'Django' in browser.title
