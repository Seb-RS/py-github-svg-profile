import requests
from datetime import datetime


class GitHubAPI:
    def __init__(self, username):
        self.username = username

    def get_contributions(self, year=None):
        if year is None:
            current_year = datetime.now().year
            url = f"https://skyline.github.com/{self.username}/{current_year}.json"
        else:
            url = f"https://skyline.github.com/{self.username}/{year}.json"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            return data

        except requests.RequestException as e:
            print(f"GitHub API request error: {e}")
            raise
