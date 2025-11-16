import requests

def get_apod():
    """Get NASA Astronomy Picture of the Day"""
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url)
    return response.json()

def get_space_weather():
    """Get basic space weather data"""
    return {
        "solar_flares": "low",
        "solar_flux": 75,
        "geomagnetic_storm": "quiet"
    }