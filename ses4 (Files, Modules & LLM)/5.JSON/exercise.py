import requests
import os
import subprocess


response = requests.get(
    "https://api.github.com/orgs/python-elective-kea/repos")

repos = response.json()

clone_urls = [repo['clone_url'] for repo in repos]
print(clone_urls)


directory_path = "5.JSON/cloned_repos"

os.makedirs(directory_path, exist_ok=True)

os.chdir(directory_path)

for url in clone_urls:
    subprocess.run(["git", "clone", url])