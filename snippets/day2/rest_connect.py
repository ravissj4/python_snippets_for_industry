import requests
import pprint # pprint is used to pretty print jsons/dicts
import pandas as pd


# working on website : https://developers.themoviedb.org/3
api_key = '1914bcb9355b5e48db537bbdade3d9eb' # version 3
api_key_v4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTE0YmNiOTM1NWI1ZTQ4ZGI1MzdiYmRhZGUzZDllYiIsInN1YiI6IjVlYzY0MjBlOTk3OWQyMDAxZjMzZjY1ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.E7qsvm0UodAbicFN7-kbIEUvMa1UQP9rUz2KTs1oGRg'

# HTTP request METHODS
"""
GET -> grab data
POST -> add/update data
PATCH
PUT
DELETE
"""

# what's our endpoint (or a url)?

# what is the HTTP method that we need?


# endpoint : 
# /movie/{movie_id}


# request example - https://api.themoviedb.org/3/movie/550?api_key=1914bcb9355b5e48db537bbdade3d9eb

### checking to see information about a specific movie via its id
# using v3
movie_id = 500
api_version = 3
base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{base_url}{endpoint_path}?api_key={api_key}&page=1'
print(endpoint)
# r = requests.get(endpoint) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)

# Using v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint, headers=headers) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)


### to go a step further, we can try to understand what these movie ids are 
### we can do that by going into the search section and searching for a specific movie

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
print(endpoint)
r = requests.get(endpoint)

if r.status_code in range(200,299):
    
    data = r.json()
    # pprint.pprint(data)
    # print(data.keys())

    results = data['results']
    # print(type(results))

    # print(results[0].keys())
    movie_ids = set()
    if len(results) > 0:
        for result in results:
            movie_id = result['id']
            movie_ids.add(movie_id)

output = 'movie_search.csv'
movies_data = []
for movie_id in movie_ids:
    api_version = 3
    base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/movie/{movie_id}'
    endpoint = f'{base_url}{endpoint_path}?api_key={api_key}'
    print(endpoint)
    r = requests.get(endpoint)
    
    if r.status_code in range(200, 299):
        data = r.json()
        movies_data.append(data)


df = pd.DataFrame(movies_data)
print(df.head())
df.to_csv(output, index=False)

'''
    So, what we did ? 
    1. First of all, searched for all the movie results of a particular movie - The matrix
    2. Store all the ids of the movies in the result. 
    3. Extracted data of all those movies 
'''