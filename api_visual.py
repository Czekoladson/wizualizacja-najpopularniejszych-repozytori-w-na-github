import requests
from plotly import offline
from plotly.graph_objects import Bar

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
header = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url,headers= header)
print(f'Kod stanu: {r.status_code}')

response_dict = r.json()

print(f'Całkowita liczba repozytoriów: {response_dict['total_count']}')

repo_dicts = response_dict['items']

repo_links,stars,labels = [],[],[]

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href ='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,20)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Projekty z największą liczbą gwiazdek na githubie',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'repozytoria',
        'titlefont': {'size': 25},
        'tickfont': {'size': 15},
    },
    'yaxis': {
        'title': 'gwiazdki',
        'titlefont': {'size': 25},
        'tickfont': {'size': 15},
    },
}

fig = { 'data': data, 'layout': my_layout}
offline.plot(fig,filename = 'python_repos.html')