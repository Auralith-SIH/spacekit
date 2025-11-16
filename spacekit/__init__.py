"""SpaceKit - Python utilities for space data and NASA/ISRO API integration."""
from .nasa import get_apod, get_space_weather

__version__ = "0.1.0"
__all__ = ["get_apod", "get_space_weather"]