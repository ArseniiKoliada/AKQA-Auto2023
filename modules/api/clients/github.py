import requests

# Base GitHub class with methods that search for a username and a repository. URL format for searches taken from GitHub API site
class GitHub:
    
    # Search for a username from all users with a GET request.
    # using json() method to return the body of the response, which is in JSON format
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    # search for a repository with a GET request, with parameter q for specifying the name of the repository,
    # return the body of the response, which is in JSON format
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body