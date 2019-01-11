import git
import requests
import os

repo = git.Repo('output')

diff = repo.index.diff('HEAD')

sites_to_check = ['website-pathology']
updated_sites = []

for file in diff:
    for s in sites_to_check:
        if s in file.a_path:
            updated_sites.append(s)
            sites_to_check.remove(s)

token = os.environ['TCI_TOKEN']

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Travis-API-Version': '3',
    'Authorization': f'token {token}'
}
body = '{"request": {"branch":"master"}}'

for site in updated_sites:
    print(f"Triggering build for {site}.")
    repo = f'DIAGNijmegen%2F{site}'
    url = f'https://api.travis-ci.org/repo/{repo}/requests'

    try:
        requests.post(url, data=body, headers=headers)
    except:
        print("Updating site failed")