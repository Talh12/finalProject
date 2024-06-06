from flask import Flask, request, jsonify, send_from_directory
import requests
import psycopg2
import os
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

API_KEY = "790975a2bf27f7201ad4b899a7631fc3"


def get_db_connection():
    conn = psycopg2.connect(
        dbname='weather_db',
        user='weather_user',
        password='talpass',
        host='localhost',
        port='5432'
    )
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id SERIAL PRIMARY KEY,
            city VARCHAR(255),
            temperature_celsius FLOAT,
            weather_condition VARCHAR(255),
            wind_speed_kmh FLOAT,
            wind_direction FLOAT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


def get_weather_by_city(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()


def get_temperature(weather_data):
    kelvin = weather_data['main']['temp']
    celsius = kelvin - 273.15
    return celsius


def get_weather_condition(weather_data):
    return weather_data['weather'][0]['main']


def get_wind(weather_data):
    speed_kmh = weather_data['wind']['speed'] * 3.6
    direction = weather_data['wind']['deg']
    return speed_kmh, direction


def save_weather_data(city, weather_data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO weather (city, temperature_celsius, weather_condition, wind_speed_kmh, wind_direction)
        VALUES (%s, %s, %s, %s, %s)
    ''', (
        city,
        get_temperature(weather_data),
        get_weather_condition(weather_data),
        get_wind(weather_data)[0],
        get_wind(weather_data)[1]
    ))

    conn.commit()
    cursor.close()
    conn.close()


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    city_weather = get_weather_by_city(city, API_KEY)

    if city_weather.get("cod") != 200:
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
    create_table()
    app.run(host='0.0.0.0', debug=True, port=8081)
