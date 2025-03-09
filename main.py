import os
from datetime import datetime
from scripts.fetch_weather import fetch_weather
from scripts.generate_script import generate_script
from scripts.create_video import create_video
from scripts.fetch_image import fetch_image
from scripts.generate_newsletter import generate_newsletter
from scripts.analyze_climate import analyze_climate
from scripts.generate_blog import generate_blog
from scripts.text_to_speech import text_to_speech
from moviepy.editor import *
from moviepy.config import change_settings
import json
from PIL import Image

# Ensure ImageMagick path is configured correctly
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

def map_weather_to_image(weather_condition):
    weather_image_map = {
        "Rain": "rainy_street.jpg",
        "Snow": "snowy_mountains.jpg",
        "Fog": "foggy_road.jpg",
        "Thunderstorm": "stormy_sky.jpg",
        "Clear sky": "sunny_park.jpg",
        "Cloudy": "cloudy_sky.jpg",
    }
    return weather_image_map.get(weather_condition, "default_weather.jpg")

def run_workflow():
    print("Fetching weather data...")
    weather_data = fetch_weather()

    print("Generating vlog script...")
    news_text = generate_script(weather_data)

    print("📸 Fetching relevant images dynamically...")
    today_date = datetime.today().strftime("%Y-%m-%d")
    folder_path = os.path.join("media", "images", today_date)
    os.makedirs(folder_path, exist_ok=True)

    weather_condition = weather_data.get('condition', 'Clear sky')
    detailed_condition = f"{weather_condition} in {weather_data.get('city', 'your city')}"
    weather_image_name = map_weather_to_image(weather_condition)

    weather_image = fetch_image(detailed_condition, os.path.join(folder_path, weather_image_name))
    city_image = fetch_image("Chennai city skyline", os.path.join(folder_path, "city.jpg"))

    if not weather_image or not city_image:
        print("❌ Image fetch failed. Using fallback images.")
        weather_image = "media/images/default_weather.jpg"
        city_image = "media/images/city.jpg"

    print("📊 Analyzing climate trends...")
    historical_data = {
        "date": "2024-02-26",
        "temperature": 28,
        "humidity": 65
    }
    climate_trends = analyze_climate(weather_data, historical_data)

    print("📰 Generating daily newsletter...")
    newsletter_path = generate_newsletter(weather_data, climate_trends)
    print(f"✅ Newsletter created at: {newsletter_path}")

    print("✍️ Generating blog post...")
    blog_path = generate_blog(weather_data, climate_trends)
    print(f"✅ Blog created at: {blog_path}")

    print("🗣️ Generating narration audio with timing data...")
    text_to_speech("media/narration.mp3", "media/subtitles.json")

    # Using the existing narration audio
    audio_path = "media/narration.mp3"
    subtitle_data_path = "media/subtitles.json"

    print("🎥 Creating video with AI voice, images, and synced subtitles...")
    video_output_path = "media/output.mp4"
    create_video_with_text_overlay(weather_image, city_image, audio_path, subtitle_data_path, video_output_path)

    print("✅ Automated vlog is ready! Check 'media/output.mp4'")

# Video Creation Function
def create_video_with_text_overlay(weather_image, city_image, audio_path, subtitle_data_path, output_video_path):
    # Grey Background
    background_clip = ColorClip(size=(1280, 720), color=(220, 220, 220)).set_duration(10)

    # Avatar (News Reader)
    avatar_image = "media/avatar.png"
    if os.path.exists(avatar_image):
        avatar_clip = ImageClip(avatar_image).set_duration(10).resize(height=400).set_position(("left", "center"))
    else:
        print("⚠️ Avatar image missing. Skipping avatar overlay.")
        avatar_clip = None

    # Weather Image (Positioned correctly on the right)
    weather_clip = ImageClip(weather_image).set_duration(10).resize(height=150).set_position(("right", 100))

    # City Image (Optional Background Element at bottom-right)
    city_clip = ImageClip(city_image).set_duration(10).resize(height=180).set_position(("right", "bottom"))

    # Combine Visual Elements
    visual_layers = [background_clip]
    if avatar_clip:
        visual_layers.append(avatar_clip)
    visual_layers.extend([weather_clip, city_clip])

    combined_visual = CompositeVideoClip(visual_layers)

    # Load audio
    audio_clip = AudioFileClip(audio_path)

    # Generate properly formatted subtitles
    with open(subtitle_data_path, 'r') as file:
        subtitle_data = json.load(file)

    subtitle_clips = []
    for entry in subtitle_data:
        subtitle_clip = TextClip(entry["text"], fontsize=30, color='white', bg_color='black')
        subtitle_clip = subtitle_clip.set_position(('center', 'bottom')).set_start(entry["start"]).set_duration(entry["duration"])
        subtitle_clips.append(subtitle_clip)

    # Combine video layers with subtitles
    final_video = CompositeVideoClip([combined_visual] + subtitle_clips).set_audio(audio_clip)

    # Save final video
    final_video.write_videofile(output_video_path, fps=24)
    print(f"✅ Vlog created successfully: {output_video_path}")

if __name__ == "__main__":
    run_workflow()