# scripts/analyze_climate.py

def analyze_climate(weather_data, historical_data):
    """Compare today's weather with historical trends."""
    temp_diff = weather_data["temperature"] - historical_data["temperature"]
    
    if temp_diff > 0:
        return f"Today's temperature is {temp_diff}°C higher than on {historical_data['date']}."
    elif temp_diff < 0:
        return f"Today's temperature is {abs(temp_diff)}°C lower than on {historical_data['date']}."
    else:
        return f"Today's temperature matches exactly with {historical_data['date']}."
