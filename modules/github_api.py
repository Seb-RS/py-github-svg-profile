import requests


class GitHubAPI:
    def __init__(self, username):
        self.username = username

    def get_contributions(self, year):
        url = f"https://skyline.github.com/{self.username}/{year}.json"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            return data

        except requests.RequestException as e:
            print(f"GitHub API request error: {e}")
            raise
