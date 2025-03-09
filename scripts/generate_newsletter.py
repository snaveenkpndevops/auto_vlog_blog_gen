import os
import pdfkit
from datetime import datetime, timedelta
import requests

# Pexels API Key
PEXELS_API_KEY = "rzOVxIGb7T2vDVcAB0li6BDKZFObsQXdWr6GGKQSUxdQwlPwmKdpBvYR"
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
        "wind_speed": 15
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

def generate_newsletter(weather_data, climate_trends):
    """Generate a visually appealing HTML newsletter with improved design."""
    if not weather_data:
        print("❌ Error: No weather data available!")
        return None

    location = weather_data["location"]
    temperature = weather_data["temperature"]
    condition = weather_data["condition"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]

    weather_image = fetch_image(f"{condition} weather")
    city_image = fetch_image(f"{location} city skyline")

    date_today = datetime.today().strftime("%A, %B %d, %Y")

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Poppins', Arial, sans-serif;
                color: #333;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: #fff;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                overflow: hidden;
            }}
            h1 {{
                background-color: #4CAF50;
                color: #fff;
                padding: 15px;
                text-align: center;
                border-radius: 8px 8px 0 0;
            }}
            .weather-info {{
                text-align: center;
                color: #0275d8;
                margin-bottom: 10px;
            }}
            .image-container img {{
                width: 100%;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .footer {{
                text-align: center;
                color: #555;
                margin-top: 20px;
                padding-top: 10px;
                border-top: 1px solid #ddd;
                font-size: 12px;
            }}
            .cta-button {{
                display: block;
                width: 100%;
                background-color: #0275d8;
                color: #fff;
                text-align: center;
                padding: 10px 0;
                margin-top: 15px;
                text-decoration: none;
                border-radius: 5px;
            }}
            .cta-button:hover {{
                background-color: #025aa5;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌤️ {location} Weather Report</h1>
            <p class="weather-info">{date_today}</p>

            <div class="image-container">
                <img src="{city_image}" alt="City View of {location}">
            </div>

            <h2>🌡️ {temperature}°C | {condition}</h2>
            <p>💧 Humidity: {humidity}% | 💨 Wind Speed: {wind_speed} km/h</p>

            <div class="image-container">
                <img src="{weather_image}" alt="Weather Condition - {condition}">
            </div>

            <h2>📊 Climate Trends</h2>
            <p>{climate_trends}</p>

            <a class="cta-button" href="https://weather.com/" target="_blank">
                🔍 View Detailed Weather Report
            </a>

            <div class="footer">
                📧 Daily Weather Newsletter | Powered by Weatherstack
            </div>
        </div>
    </body>
    </html>
    """

    os.makedirs("newsletter", exist_ok=True)
    newsletter_path = "newsletter/weather_newsletter.html"

    with open(newsletter_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"✅ Modern Newsletter generated: {newsletter_path}")

    # Convert HTML to PDF using pdfkit
    pdf_path = "newsletter/weather_newsletter.pdf"
    try:
        pdfkit.from_file(newsletter_path, pdf_path)
        print(f"✅ PDF generated: {pdf_path}")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")

    return newsletter_path

def run_workflow():
    """Main workflow to generate the newsletter and PDF."""
    print("Fetching weather data...")
    weather_data = fetch_weather_data()

    print("Fetching historical weather data...")
    historical_weather = fetch_historical_weather()

    print("Comparing weather data...")
    climate_trends = compare_weather(weather_data, historical_weather)

    print("📰 Generating daily newsletter...")

    newsletter_path = generate_newsletter(weather_data, climate_trends)

    if newsletter_path:
        print(f"✅ Newsletter saved at {newsletter_path}")

if __name__ == "__main__":
    run_workflow()
