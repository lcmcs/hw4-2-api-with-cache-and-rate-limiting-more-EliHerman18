import os
import requests
from dotenv import load_dotenv
import time


CACHE = {}

def get_weather_cached(city):
    """Get weather with caching."""
    cache_key = city.lower()

    if cache_key in CACHE:
        print(f"Cache was used for {city}")
        return CACHE[cache_key]

    time.sleep(0.5)
    weather, code = get_weather(city)
    country = get_country_info(code)

    if weather:
        CACHE[cache_key] = [weather, country]

    return weather, country

# 1. Load the secret API_KEY
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Fetches weather and returns a tuple: (weather_data, country_code)
def get_weather(city):

    #checking that there is an API_KEY
    if not API_KEY:
        return None, None
    #setting up the url
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    try:
        #requsttung info from url
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Error: City '{city}' not found.")
            return None, None
        #formating the output from the web
        data = response.json()

        #Getting the country code to pass to the next API
        country_code = data["sys"]["country"]

        return {"temperature": data['main']['temp'],
                "conditions": data['weather'][0]['description'],
                "humidity": data['main']['humidity'],
                "wind": data['wind']['speed']}, country_code

    except Exception as e:
        print(f"Weather API Error: {e}")
        return None, None


def get_country_info(code):

    #Useing the country code to get data from REST Countries API
    url = f"https://restcountries.com/v3.1/alpha/{code}"

    try:
        response = requests.get(url)
        # [0] bec it's a list
        country = response.json()[0]
        # since we don't know if it will be eur or usd we just grab the values and put tem in a list
        # (list ... [0] grabs the first one if there's more than one)
        currency_data = list(country["currencies"].values())[0]
        #formatting for later
        currency_string = f"{currency_data['name']} ({currency_data.get('symbol', '')})"
        #puts all the langs into a list
        languages = list(country["languages"].values())
        #adds the items together (if there's only one thing in the list it does nothing)
        language_string = ", ".join(languages)
        # returning as a dictionary inorder to safely return multiple things
        return {
            "name": country['name']['common'],
            "official_name": country['name']['official'],
            "capital": country['capital'][0],  # Capital is also a list
            "population": country['population'],
            "languages": language_string,
            "currency": currency_string
        }
    except Exception as e:
        print(f"Country API Error: {e}")
        return None


def main():
    print("TRAVEL INFO DASHBOARD")

    city = "none"
    cached_citys = 0
    api_citys = 0
    citys_in_cache = []

    while city.lower() != "quit":
        city = input("Enter a city (or 'quit' to exit): ")

        if city.lower() == "quit":
            print(f"Cities fetched from API: {api_citys} | Cities served from cache: {cached_citys}")
        else:
            weather, country = get_weather_cached(city)

            if weather and country:
    
                if city.lower() in citys_in_cache:
                    cached_citys += 1
                else:
                    api_citys += 1
                    citys_in_cache.append(city.lower())

                # Step 3: Print formatted output
                print(f"\n📍 {city.upper()}, {country['name'].upper()}\n")

                print("🌤️  WEATHER")
                print(f"   Temperature:    {weather['temperature']}°F")
                print(f"   Conditions:     {weather['conditions']}")
                print(f"   Humidity:       {weather['humidity']}%")
                print(f"   Wind:           {weather['wind']} MPH\n")

                print("🏳️  COUNTRY INFO")
                print(f"   Official name:  {country['official_name']}")
                print(f"   Capital:        {country['capital']}")
                print(f"   Population:     {country['population']:,}")
                print(f"   Languages:      {country['languages']}")
                print(f"   Currency:       {country['currency']}")
                print()
            else:
                print("Could not retrieve country details.")

main()