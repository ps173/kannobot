import requests
import json


def search_anime(name):
    try:
        res = requests.get(
            f"https://api.jikan.moe/v3/search/anime?q={name}&page=1")
        string = json.dumps(res.json())
        results = json.loads(string)['results']
        return results[0]
    except:
        return "Probably Not found"


def search_manga(name):
    try:
        res = requests.get(
            f"https://api.jikan.moe/v3/search/manga?q={name}&page=1")
        string = json.dumps(res.json())
        results = json.loads(string)['results']
        return results[0]
    except:
        return "Probably Not found"


if __name__ == "__main__":
    # temperory tests
    import sys
    print(search_manga(sys.argv[1]))
    print(search_anime(sys.argv[1]))
