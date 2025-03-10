Install python --> My current version is Python 3.12.3

cd weather_vlog_prototype_dropped

python -m venv venv

source venv/Scripts/activate

pip install requests

python.exe -m pip install --upgrade pip

pip install nltk

pip install moviepy==1.0.3

pip install pyttsx3

pip install pdfkit

Download link: WKHTMLTOPDF for windows and install.




pip install --upgrade Pillow



python main.py

```

Replace this line inside venv\Lib\site-packages\moviepy\video\fx\resize.py

resized_pil = pilim.resize(newsize[::-1], Image.ANTIALIAS)

with 

resized_pil = pilim.resize(newsize[::-1], Image.LANCZOS)
```


---



pip freeze > requirements.txt


pip install -r requirements.txt


Pre-requisite:

1. In scripts/fetch_weather.py  --> Get the weather data from weather stack

[For this get the api key from weather stack website]

url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={LOCATION}"


2.  In scripts/create_video.py  --> Generate Video using HeyGen Website

[For this get the api key from HeyGen website]

HEYGEN_API_URL = "https://api.heygen.com/v1/video/generate"


3. In scripts/download_images.py  --> download the content related images from SerpApi: Google Search API

[For this get the api key from SerpApi website]

SERPAPI_KEY

[or]

 In scripts/fetch_image.py  --> fetch the content related images from PEXELS 

[For this get the api key from PEXELS website]

PEXELS_URL = "https://api.pexels.com/v1/search"


4.  In scripts/generate_blog.py  --> Generate the weather related blog using PEXELS 

[For this get the api key from PEXELS website]


PEXELS_URL = "https://api.pexels.com/v1/search"


5. In scripts/generate_newsletter.py  --> Generate the weather related newsletter using PEXELS 

[For this get the api key from PEXELS website]


PEXELS_URL = "https://api.pexels.com/v1/search"


6. 

