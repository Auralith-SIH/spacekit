"""
SpaceKit - Python utilities for space data and NASA/ISRO API integration.
"""

from .nasa import get_apod, get_apod_safe, get_space_weather
from .astronomy import satellite_position

__version__ = "0.1.0"
__all__ = [
    "get_apod",
    "get_apod_safe", 
    "get_space_weather",
    "satellite_position"
]