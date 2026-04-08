import json
from urllib.request import Request, urlopen

API_URL = 'https://api.chucknorris.io/jokes/random'
REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0'}

def main() -> None:
    try:
        request = Request(API_URL, headers=REQUEST_HEADERS)
        with urlopen(request, timeout=10) as response:
            data = json.load(response)
            joke = data.get('value', '')
    except Exception:
        joke = 'unable to fetch a Chuck Norris joke at this time.' #idont have to use the visual keyboard anymore, yay.
    print(joke)

if __name__ == '__main__':
    main()
