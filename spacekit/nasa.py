import requests

DEMO_KEY = "DEMO_KEY"

def get_apod(api_key=DEMO_KEY):
    url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': api_key}
    try:
        response = requests.get(url, params=params, timeout=10)
        return response.json()
    except:
        return {"title": "SpaceKit Demo", "url": "", "error": True}

def get_apod_safe():
    data = get_apod()
    if data.get('error'):
        return {
            "title": "Welcome to SpaceKit!",
            "url": "https://example.com/space.jpg",
            "demo": True
        }
    return data

def get_space_weather():
    return {
        "solar_flares": "low",
        "status": "normal"
    }