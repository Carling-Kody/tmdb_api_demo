import requests
import os

BASE_URL = 'https://api.themoviedb.org/3'

def test_discover_movie():
    headers = {"Authorization": "Bearer {}".format(os.environ.get("API_KEY"))}
    
    params = {
        "page": 1,
        "language": "en-US",
        "sort_by": "popularity.desc",
         "include_adult": "false"
         }
    response = requests.get(
        BASE_URL + "/discover/movie", headers=headers, params=params
        )

    assert response.status_code == 200

def test_discover_tv():
    pass
