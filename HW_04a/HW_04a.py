import json

import requests


def search_repo(the_username):
    repo = []
    link = 'https://api.github.com/users/' + the_username + '/repos'
    print(link)
    github_data = requests.get(link)
    data = github_data.json()
    for i in data:
        repo.append(i['name'])
    for z in repo:
        link2 = 'https://api.github.com/repos/' + the_username + '/' + z + '/commits'
        github_data2 = requests.get(link2)
        data2 = github_data2.json()
        count = len(data2)
        print(z, '---->', count)
    return len(repo)


def main():
    username = input("GitHub ID: ")
    search_repo(username)


if __name__ == '__main__':
    main()
