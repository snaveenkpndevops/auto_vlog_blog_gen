import os
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize

# Ensure required NLTK packages are available
def download_nltk_data():
    required_packages = [
        "punkt", 
        "averaged_perceptron_tagger", 
        "maxent_ne_chunker", 
        "words", 
        "punkt_tab"
    ]
    for package in required_packages:
        nltk.download(package, quiet=True)  # Quiet mode to avoid extra output

# ✅ Download missing NLTK dependencies before use
download_nltk_data()

def extract_relevant_weather_info(script):
    """Filters out the most relevant weather information only."""
    
    # Define important keywords related to weather
    weather_keywords = [
        "temperature", "humidity", "wind speed", "forecast", "rain", "storm", "sunny",
        "cloudy", "thunderstorm", "climate", "weather", "pressure", "visibility"
    ]
    
    # Tokenize script into sentences
    sentences = sent_tokenize(script)

    # Filter sentences that contain key weather-related words
    relevant_sentences = [sentence for sentence in sentences if any(word in sentence.lower() for word in weather_keywords)]

    # Join the filtered sentences
    filtered_script = " ".join(relevant_sentences)

    return filtered_script.strip()

def generate_script(weather_data):
    url = "http://localhost:11434/api/generate"
    model_name = "mistral"  # Change to "llama3" if needed

    payload = {
        "model": model_name,
        "prompt": f"Generate a detailed yet concise weather update based on this data: {weather_data}. Only include the most relevant details.",
        "stream": False
    }

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        raw_script = result.get("response", "No response from model.")

        # ✅ Extract only the most relevant weather-related content
        cleaned_script = extract_relevant_weather_info(raw_script)

        # ✅ Ensure 'data' directory exists
        os.makedirs("data", exist_ok=True)

        # ✅ Save cleaned script
        script_path = os.path.join("data", "vlog_script.txt")
        with open(script_path, "w", encoding="utf-8") as file:
            file.write(cleaned_script)

        print("✅ Script saved successfully with only the most relevant content!")
        return cleaned_script
    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        print(error_message)
        return error_message
