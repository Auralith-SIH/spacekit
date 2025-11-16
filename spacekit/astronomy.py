def satellite_position(satellite_name):
    """
    Get satellite position (simulated data).
    
    Args:
        satellite_name (str): Name of the satellite (e.g., 'ISS')
    
    Returns:
        dict: Satellite position data
    """
    if satellite_name.upper() == "ISS":
        return {
            "latitude": 28.61, 
            "longitude": 77.23, 
            "altitude": 408,
            "name": "International Space Station"
        }
    return {
        "latitude": 0, 
        "longitude": 0, 
        "altitude": 0,
        "name": satellite_name
    }