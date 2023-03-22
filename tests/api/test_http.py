import pytest
import requests
import sys
# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')



# perform a GET request at GitHub API Zen page, printing text from the response
@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response: {r.text}")

# search for a username "defunkt", print all user attributes through json method and response headers with headers parameter 
@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

# check if name parameter, response code and Server parameter of the response are 'Chris Wanstrath', 200 and 'Github.com' respectively
    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'
    # print(f"Response body: {r.json()}")
    # print(f"Response status code: {r.status_code}")
    # print(f"Response headers: {r.headers}")

# check that a response code is 404 for inexistent repository
@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404