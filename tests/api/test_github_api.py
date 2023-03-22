# import pytest and GitHub class to use it's methods
import pytest
from modules.api.clients.github import GitHub

#   Using the GitHub class and github_api fixture, need only to insert the fixture's name when defining a test, \
#    only a username when searching for a user and only a repository name when searching for repositories
# check if a certain user exists by searching for an existing username
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

# check if a certain user does not exist by searching for an inexisting username
@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'
    print (r['message'])

# check that a certin repository exists by searching for an existing repository name
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 26
    assert 'become-qa-auto' in r['items'][0]['name']


# check that a certin repository does not exist by searching for an inexisting repository name
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

# check if there are any (above zero) existing repositories whose names consist of a single character
@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0