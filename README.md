# 🌦️ Weather Vlog, Blog and Newsletter Automation

This Python project automates the process of creating a weather vlog by integrating weather data, images, text narration, and video creation. It simplifies the content creation workflow with minimal manual intervention.

---

## 🚀 Features

✅ Automated weather data fetching  
✅ Dynamic text script generation based on weather insights  
✅ Image fetching via Pexels API for visuals  
✅ Climate trend analysis using historical data  
✅ Automated newsletter and blog post creation  
✅ AI-narrated video with text overlays  

---

## 🛠️ Tools Used

- **Python** - Core language for the automation logic
- **MoviePy** - For video editing and overlay generation
- **Pexels API** - For fetching relevant weather and city images
- **Weatherstack API** - For fetching real-time weather data
- **Pexels API & PDFKit** - For generating blog posts and newsletters
- **NLTK, NLP, and Olama Mistral Model** - For generating text scripts with AI language capabilities
- **Pyttsx3** - For converting text to speech (AI narration)

---

## 🏗️ Project Structure

```
├── media
│   ├── images
│   │   └── [date]
│   ├── narration.mp3
│   ├── default_weather.jpg
│   ├── default_city.jpg
│   └── output.mp4
├── scripts
│   ├── fetch_weather.py
│   ├── generate_script.py
│   ├── create_video.py
│   ├── fetch_image.py
│   ├── generate_newsletter.py
│   ├── analyze_climate.py
│   └── generate_blog.py
├── main.py
└── requirements.txt
```

---

## ⚙️ Prerequisites

Before running the project, ensure you have the following:

- **Python 3.10+**
- **ImageMagick** installed (for text rendering in `moviepy`)
- Required Python libraries (install with the command below)

```bash
pip install -r requirements.txt
```

---

## 📄 Configuration

Ensure ImageMagick is correctly set up:

In your `main.py` file, update this path if needed:
```python
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
```

---

## ▶️ Usage

To run the complete workflow:

```bash
python main.py
```

### Output
✅ Newsletter will be generated in `/newsletter/weather_newsletter.html` and ``/newsletter/weather_newsletter.pdf`
✅ Blog post will be saved in `/blog/index.html` and  `/blog/weather_blog.pdf`
✅ Final Vlog video will be saved as `/media/output.mp4`  


---

### Newsletter Screenshot

![Newsletter Screenshot](images/newsletter1.png)


![Newsletter Screenshot](images/newsletter2.png)


![Newsletter Screenshot](images/newsletter3.png)







### Blog Screenshot


![Blog Screenshot](images/blog1.png)


![Blog Screenshot](images/blog2.png)





### Vlog Output


🎬 [Watch the Vlog Video](media/output.mp4)

---



## 🔧 Troubleshooting

**1. Image Fetch Failure**  
- If the Pexels image fetch fails, the system will automatically switch to fallback images.

**2. Video Creation Issues**  
- Ensure `ImageMagick` path is configured correctly in `main.py`

**3. Missing Libraries**  
- Run `pip install -r requirements.txt` to install dependencies.

---

## 💬 Feedback & Contributions
Contributions are welcome! Feel free to submit pull requests or report issues.

For queries, contact Naveen via snaveenkpn@gmail.com.
