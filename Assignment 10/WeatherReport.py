import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def main() -> None:
    api_key = os.getenv('OPENWEATHER_API_KEY') or input('API key: ').strip()
    if not api_key:
        raise SystemExit('Register at https://openweathermap.org/api and provide a key.')
    city = input('municipality: ').strip()
    if not city:
        raise SystemExit('municipality name required.')
    url = f'{API_URL}?{urlencode({'q': city, 'appid': api_key})}'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urlopen(req, timeout=10) as response:
            data = json.load(response)
    except HTTPError as error:
        raise SystemExit(f'HTTP {error.code}: {error.reason}')
    except URLError as error:
        raise SystemExit(f'network error: {error.reason}')
    weather = data['weather'][0]['description'].capitalize()
    celsius = data['main']['temp'] - 273.15
    print(f'Weather Report: {weather}, {celsius:.1f}°C')
#I have put a JoJo ref into this code.
#for some reason, my API key cant access to the weather data, even tho i have create a account.
if __name__ == '__main__':
    main()
