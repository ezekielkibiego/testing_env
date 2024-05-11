import requests

response = requests.get('https://api.github.com/users/ezekielkibiego/repos')
repos = response.json()

for repo in repos:
    print(repo['name'])
    print(repo['html_url'])
