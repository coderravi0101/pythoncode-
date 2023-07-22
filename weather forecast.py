import requests

def get_weather_forecast(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace this with your actual API key
    city_name = "lucknow"    # Replace this with the desired city name

    weather_data = get_weather_forecast(api_key, city_name)
    if weather_data:
        print(f"Weather forecast for {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to fetch weather data.")