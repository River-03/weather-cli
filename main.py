import requests

API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city_name):
    try:
        params = {'q': city_name, 'appid': API_KEY, 'units': 'metric', 'lang': 'en'}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather_info = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'desc': data['weather'][0]['description'].title(),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }

        print(f"\n🌤️ Weather in {weather_info['city']}:")
        print(f"🌡️ Temperature: {weather_info['temp']}°C")
        print(f"🌥️ Condition: {weather_info['desc']}")
        print(f"💧 Humidity: {weather_info['humidity']}%")
        print(f"💨 Wind Speed: {weather_info['wind_speed']} m/s\n")

    except requests.exceptions.ConnectionError:
        print("❌ Unable to connect to the server. Please check your internet connection.")
    except requests.exceptions.InvalidURL:
        print("❌ Invalid API URL. Please check the service provider.")
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("🏙️ City not found. Please enter a valid city name.")
        else:
            print(f"⚠️ HTTP Error occurred: {err}")
    except Exception as e:
        print(f"❗ An unexpected error occurred: {e}")


if __name__ == '__main__':
    city = input("🌆 Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("❌ No city entered. Please provide a valid city name.")