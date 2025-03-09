import os
import pdfkit  # Import pdfkit
from datetime import datetime, timedelta
import requests

PEXELS_API_KEY = "rzOVxIGb7T2vDVcAB0li6BDKZFObsQXdWr6GGKQSUxdQwlPwmKdpBvYR"  # ✅ Replace with your real API key
PEXELS_URL = "https://api.pexels.com/v1/search"

def fetch_image(query):
    """Fetch an image URL from Pexels."""
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1}

    try:
        response = requests.get(PEXELS_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["photos"]:
            return data["photos"][0]["src"]["medium"]
        else:
            return "https://via.placeholder.com/600x300"  # Fallback image
        
    except Exception as e:
        print(f"❌ Image fetch error: {e}")
        return "https://via.placeholder.com/600x300"  # Fallback image

def fetch_weather_data():
    """Simulated weather data retrieval."""
    return {
        "location": "New York",
        "temperature": 22,
        "condition": "Sunny",
        "humidity": 60,
        "wind_speed": 15,
        "uv_index": 5,
        "sunrise": "6:30 AM",
        "sunset": "7:45 PM"
    }

def fetch_historical_weather(days_ago=5):
    """Simulated historical weather data retrieval."""
    historical_date = (datetime.today() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
    return {
        "date": historical_date,
        "temperature": 20,  
        "condition": "Partly Cloudy",
    }

def compare_weather(today, historical):
    """Compare today's weather with historical data."""
    temp_diff = today["temperature"] - historical["temperature"]
    temp_trend = (
        f"Today is {abs(temp_diff)}°C {'warmer' if temp_diff > 0 else 'cooler'} than {historical['date']}."
    )
    condition_trend = f"Today's weather is {today['condition'].lower()} compared to {historical['condition'].lower()} {historical['date']}."
    
    return f"{temp_trend} {condition_trend}"

def generate_blog(weather_data, climate_trends):
    """Generate a dynamic blog post about the weather."""

    if not weather_data:
        print("❌ Error: No weather data available!")
        return None

    location = weather_data["location"]
    temperature = weather_data["temperature"]
    condition = weather_data["condition"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    uv_index = weather_data.get("uv_index", "N/A")  # Provide a default value if missing
    sunrise = weather_data.get("sunrise", "N/A")
    sunset = weather_data.get("sunset", "N/A")


    weather_image = fetch_image(f"{condition} weather")
    city_image = fetch_image(f"{location} city skyline")

    date_today = datetime.today().strftime("%A, %B %d, %Y")

    blog_content = f"""
    <html>
    <head>
        <title>Weather Blog | {date_today}</title>
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; background: #f4f4f4; padding: 20px; }}
            .container {{ max-width: 800px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #0275d8; text-align: center; }}
            .weather-info, .extra-info {{ text-align: center; }}
            .image-container img {{ width: 100%; border-radius: 8px; }}
            .footer {{ text-align: center; font-size: 12px; color: #888; margin-top: 20px; }}
            .quote {{ font-style: italic; color: #555; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌎 Weather Insights: {location} - {date_today}</h1>
            
            <div class="image-container">
                <img src="{city_image}" alt="City View">
            </div>
            
            <h2>🌡️ {temperature}°C | {condition}</h2>
            <p>💧 Humidity: {humidity}% | 💨 Wind Speed: {wind_speed} km/h</p>
            <p>☀️ UV Index: {uv_index} | 🌅 Sunrise: {sunrise} | 🌇 Sunset: {sunset}</p>

            <div class="image-container">
                <img src="{weather_image}" alt="Weather Condition">
            </div>
            
            <h2>📊 Climate Trends</h2>
            <p>{climate_trends}</p>

            <h2>⚠️ Weather Safety Tips</h2>
            <p>1️⃣ Stay hydrated and avoid direct sun exposure during peak hours.</p>
            <p>2️⃣ Carry an umbrella or sunscreen for protection.</p>
            <p>3️⃣ Keep an eye on weather alerts for any sudden changes.</p>
            
            <h2>🌍 Fun Weather Fact</h2>
            <p>Did you know? The highest recorded temperature on Earth was 56.7°C (134°F) in Death Valley, USA!</p>

            <blockquote class="quote">
                "The best thing one can do when it's raining is to let it rain." - Henry Wadsworth Longfellow
            </blockquote>

            <p>Stay prepared and have a fantastic day! 😊</p>
            
            <div class="footer">
                <p>🌍 Weather Blog | Powered by Weatherstack</p>
            </div>
        </div>
    </body>
    </html>
    """

    os.makedirs("blog", exist_ok=True)
    blog_path = "blog/index.html"
    
    with open(blog_path, "w", encoding="utf-8") as file:
        file.write(blog_content)
    
    print(f"✅ Blog post generated: {blog_path}")
    
    # Convert HTML to PDF
    pdf_path = "blog/weather_blog.pdf"
    try:
        pdfkit.from_file(blog_path, pdf_path)  # Convert HTML file to PDF
        print(f"✅ PDF blog post saved at {pdf_path}")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
    
    return pdf_path

def run_blog_workflow():
    """Main workflow to generate the weather blog."""
    print("Fetching weather data...")
    weather_data = fetch_weather_data()

    print("Fetching historical weather data...")
    historical_weather = fetch_historical_weather()

    print("Comparing weather data...")
    climate_trends = compare_weather(weather_data, historical_weather)

    print("📝 Generating blog post...")
    pdf_path = generate_blog(weather_data, climate_trends)

    if pdf_path:
        print(f"✅ PDF blog saved at {pdf_path}")

if __name__ == "__main__":
    run_blog_workflow()
