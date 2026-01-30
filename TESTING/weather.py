import requests
def get_weather_data(city):
    api_url = f"https://api.weather.com/v1/{city}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    raise ValueError("Could not fetch the weather data")


