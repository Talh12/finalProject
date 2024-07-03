from flask import Flask, request, jsonify, send_from_directory
import requests
from pymongo import MongoClient
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", "790975a2bf27f7201ad4b899a7631fc3")  
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
MONGO_DB = os.getenv("MONGO_DB", "weather_db")
MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "password")

def get_db_connection():
    client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin")
    db = client[MONGO_DB]
    return db

def get_weather_by_city(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None

def get_temperature(weather_data):
    if weather_data and 'main' in weather_data and 'temp' in weather_data['main']:
        kelvin = weather_data['main']['temp']
        celsius = kelvin - 273.15
        return celsius
    return None

def get_weather_condition(weather_data):
    if weather_data and 'weather' in weather_data and len(weather_data['weather']) > 0:
        return weather_data['weather'][0]['main']
    return None

def get_wind(weather_data):
    if weather_data and 'wind' in weather_data:
        speed_kmh = weather_data['wind']['speed'] * 3.6
        direction = weather_data['wind'].get('deg', 0)  
        return speed_kmh, direction
    return None, None

def save_weather_data(city, weather_data):
    db = get_db_connection()
    weather_collection = db.weather
    data_to_save = {
        "city": city,
        "temperature_celsius": get_temperature(weather_data),
        "weather_condition": get_weather_condition(weather_data),
        "wind_speed_kmh": get_wind(weather_data)[0],
        "wind_direction": get_wind(weather_data)[1]
    }
    weather_collection.insert_one(data_to_save)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    city_weather = get_weather_by_city(city, API_KEY)

    if not city_weather or city_weather.get("cod") != 200:
        return jsonify({"error": "City not found or API request failed."}), 404

    weather_data = {
        "city": city,
        "temperature": get_temperature(city_weather),
        "weather_condition": get_weather_condition(city_weather),
        "wind_speed_kmh": get_wind(city_weather)[0],
        "wind_direction": get_wind(city_weather)[1]
    }

    save_weather_data(city, city_weather)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8081)
