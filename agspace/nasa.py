import requests

DEMO_KEY = "DEMO_KEY"
APOD_URL = "https://api.nasa.gov/planetary/apod"


def get_apod(api_key: str = DEMO_KEY) -> dict:
    """
    Fetch NASA Astronomy Picture of the Day (APOD).

    Returns a dict. On failure, returns a dict with `error=True`.
    """
    params = {"api_key": api_key}

    try:
        res = requests.get(APOD_URL, params=params, timeout=10)
        res.raise_for_status()  # fails for 4xx/5xx
        data = res.json()

        # If NASA returns an error payload, normalize it
        if isinstance(data, dict) and ("error" in data and data["error"]):
            return {"title": "NASA APOD Error", "url": "", "error": True, "details": data["error"]}

        return data

    except requests.RequestException as e:
        return {"title": "SpaceKit Demo", "url": "", "error": True, "details": str(e)}
    except ValueError:
        # JSON decode error
        return {"title": "SpaceKit Demo", "url": "", "error": True, "details": "Invalid JSON response"}


def get_apod_safe() -> dict:
    """
    Safe APOD fetch.
    Always returns a dict with at least a title + url-like field.
    """
    data = get_apod()

    # treat missing title/url as failure too
    if data.get("error") or not data.get("title"):
        return {
            "title": "Welcome to agspace!",
            "url": "https://example.com/space.jpg",
            "demo": True,
        }

    return data


def get_space_weather() -> dict:
    """
    Prototype space weather output (simulated).
    """
    return {"solar_flares": "low", "status": "normal", "source": "simulated"}