# Weather App Testing

This repository contains automated tests for the Weather App API endpoints. These tests ensure the reliability and correctness of the app's functionalities.

## Tests Overview

### Purpose
The tests aim to verify the functionality of the Weather App API, specifically focusing on:
- Retrieving weather data by city
- Extracting temperature information
- Checking weather conditions
- Fetching wind details
- Saving weather data to a database

Each test case is designed to validate a specific endpoint or function of the Weather App.

### Test Details
1. **test_get_weather_by_city.py**: This test checks the `/weather` endpoint, which retrieves weather data for a given city using the app's API.

2. **test_get_temperature.py**: Verifies the accuracy of temperature retrieval using the `/temperature` endpoint.

3. **test_get_weather_condition.py**: Tests the `/weather-condition` endpoint to ensure correct weather condition information is returned.

4. **test_get_wind.py**: Validates the `/wind` endpoint functionality, ensuring accurate wind data retrieval.

5. **test_save_weather_data.py**: This test case focuses on saving weather data to a MongoDB database using the `/save-data` endpoint. It verifies data persistence and integrity.

### Why Docker Compose?
Docker Compose is used to set up a development environment that closely mirrors the production environment. It allows us to:
- Easily manage and orchestrate multiple services (app, database).
- Ensure consistent testing environments across different machines and deployments.
- Simulate real-world conditions for testing the Weather App's integration with MongoDB.

### Running Tests
To run the tests locally using Docker Compose:
1. Ensure Docker and Docker Compose are installed on your system.
2. Clone this repository.
3. Navigate to the repository directory.
4. Run `docker-compose up --build` to build and start the application and test containers.
5. Tests will automatically execute within the Docker containers. Results will be displayed in the console.
6. After testing, you can stop the containers by pressing `Ctrl + C` and running `docker-compose down`.

### Dependencies
- Python 3.12
- Flask
- pytest
- requests
- pymongo

### Notes
- **Warning**: The Docker Compose setup is intended for development and testing purposes. Do not use in a production environment without appropriate configuration changes.

For detailed test results and logs, refer to the test output in the console.

