import requests


def search_movies_total(substr):
    url = f"https://jsonmock.hackerrank.com/api/moviesdata/search/?Title={substr}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["total"]
    else:
        print("Error:", response.status_code)
        return None


# Example usage:
substr = "maze"
total_movies = search_movies_total(substr)
if total_movies is not None:
    print("Total Movies:", total_movies)
