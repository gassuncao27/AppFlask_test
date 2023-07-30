import requests

def obter_filmes_populares(api_key):
    url = f'https://api.themoviedb.org/3/discover/movie'
    parametros = {
        'sort_by': 'popularity.desc',
        'api_key': api_key
    }

    response = requests.get(url, params=parametros)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Falha na requisição: Status Code {response.status_code}')
        return None
    
jsondata = obter_filmes_populares('01dc9daadb0119d64a803f9c74b9d8cf')

print(jsondata['results'])
