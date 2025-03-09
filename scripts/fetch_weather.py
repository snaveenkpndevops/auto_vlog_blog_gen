import requests

def fetch_weather():
    API_KEY = "f90a937e82a54ea6dff58962ee0f8dab"  # 🔹 Replace with your Weatherstack API key
    LOCATION = "Chennai"

    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={LOCATION}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # ✅ Handle API errors
        if "error" in data:
            print(f"❌ API Error: {data['error']['info']}")
            return None

        # ✅ Extract weather details
        weather_data = {
            "location": data["location"]["name"],
            "temperature": data["current"]["temperature"],
            "condition": data["current"]["weather_descriptions"][0],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_speed"]
        }
        return weather_data

    except Exception as e:
        print(f"❌ Error fetching weather data: {e}")
        return None
