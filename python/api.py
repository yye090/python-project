import requests
import pprint
import pandas as pd
api_key = "c3670e4fa48289c35c2c77d1280fec0c"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMzY3MGU0ZmE0ODI4OWMzNWMyYzc3ZDEyODBmZWMwYyIsInN1YiI6IjYyOWVlZDkyNDk4ZWY5MDA2NWZiMTI3ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.p0KUEAzq1r1Bybq7M3RS4C98UxSGT1mHA2e5Mkoq7jw"

api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))
output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)