import requests


def fetch_data(url):
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    data = fetch_data("https://www.google.com")
    print(data)
