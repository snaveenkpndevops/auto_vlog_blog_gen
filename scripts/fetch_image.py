import requests
import os

PEXELS_API_KEY = "rzOVxIGb7T2vDVcAB0li6BDKZFObsQXdWr6GGKQSUxdQwlPwmKdpBvYR"  # ✅ Replace with your actual Pexels API Key
PEXELS_URL = "https://api.pexels.com/v1/search"

def fetch_image(query, save_path):
    """Fetches an image from Pexels based on the search query"""
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1}

    try:
        response = requests.get(PEXELS_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["photos"]:
            image_url = data["photos"][0]["src"]["large"]
            img_data = requests.get(image_url).content
            
            with open(save_path, "wb") as f:
                f.write(img_data)
            
            print(f"✅ Image saved: {save_path}")
            return save_path
        else:
            print(f"❌ No images found for: {query}")
            return None
    except requests.RequestException as e:
        print(f"❌ Image fetch error: {e}")
        return None
