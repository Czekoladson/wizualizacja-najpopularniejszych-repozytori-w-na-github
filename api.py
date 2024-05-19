import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplications/vnd.github.v3+json'}
r = requests.get(url,headers = headers)
print(f'Kod stanu: {r.status_code}')

response_dict = r.json()

print(f'Całkowita liczba repozytooriów {response_dict['total_count']}')

repo_dicts = response_dict['items']
print(f'Liczba zwróconych repozytoriów {len(repo_dicts)}')



for i, repo_dict in enumerate(repo_dicts,start = 1):
    print(f'info o {i} repo: ')
    print(f'Nazwa {repo_dict['html_url']}')
    print(f'login {repo_dict['owner']['login']}')
    print(f'stworzył {repo_dict['created_at']}')
    print(f'================================')

