import sys
import os
import pytest
from unittest.mock import patch, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.main import get_weather_by_city, get_temperature, get_weather_condition, get_wind, save_weather_data

# Mock data for testing
weather_data_example = {
    'main': {'temp': 300},
    'weather': [{'main': 'Clear'}],
    'wind': {'speed': 5, 'deg': 90}
}

# Test get_weather_by_city function
@patch('app.main.requests.get')
def test_get_weather_by_city(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = weather_data_example
    mock_get.return_value = mock_response

    city = 'London'
    api_key = 'fake_api_key'
    result = get_weather_by_city(city, api_key)

    # Check that the get method was called with the base URL and parameters
    mock_get.assert_called_once_with('http://api.openweathermap.org/data/2.5/weather', params={"q": city, "appid": api_key})
    assert result == weather_data_example

# Test get_temperature function
def test_get_temperature():
    result = get_temperature(weather_data_example)
    assert result == pytest.approx(26.85, rel=1e-2)  # Use pytest.approx for approximate comparison

# Test get_weather_condition function
def test_get_weather_condition():
    result = get_weather_condition(weather_data_example)
    assert result == 'Clear'

# Test get_wind function
def test_get_wind():
    result = get_wind(weather_data_example)
    assert result == (18, 90)  # 5 m/s * 3.6 = 18 km/h, 90 degrees

# Test save_weather_data function
@patch('app.main.get_db_connection')
def test_save_weather_data(mock_get_db_connection):
    mock_db = MagicMock()
    mock_get_db_connection.return_value = mock_db

    city = 'London'
    save_weather_data(city, weather_data_example)

    mock_get_db_connection.assert_called_once()
    mock_db.weather.insert_one.assert_called_once()
    data_inserted = mock_db.weather.insert_one.call_args[0][0]
    assert data_inserted['city'] == city
    assert data_inserted['temperature_celsius'] == pytest.approx(26.85, rel=1e-2)  # Use pytest.approx for approximate comparison
    assert data_inserted['weather_condition'] == 'Clear'
    assert data_inserted['wind_speed_kmh'] == 18
    assert data_inserted['wind_direction'] == 90

if __name__ == "__main__":
    pytest.main()
