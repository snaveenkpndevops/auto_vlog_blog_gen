1. Create Folder Structure (refer chatgpt folder structure) 
2. Installation -->  pip install requests gtts moviepy openai
3. install venv  -->  python -m venv venv
4. open bash terminal and activate the venv --> source new_venv/Scripts/activate

5. Open powershell and install ffmpeg  --> choco install ffmpeg -y

[FFmpeg is a multimedia framework used for processing, converting, and streaming audio and video.]

6. Paste the code inside all the files in scripts folder.

7. Create account in openweathermap and generate api key.

[But i am using weatherstack api]

In fetch_weather.py --> update the api url.

[URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"]

to

URL = f"http://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=24f9e491ffa831c48d74d7afd79eede5&units=metric"

8. Create account in OpenAI API and generate api key.

In generate_script.py --> update the api url.

9. install --> pip install requests

10. install --> pip install openai


11. install --> pip install gtts

12. install -->  pip install moviepy

https://weatherstack.com/dashboard    [Fetch Weather report]


APIkey: 1cc9d31120d830462ee350ef6434b97d



https://www.pexels.com/api/key/      [FOR Newsletter]

rzOVxIGb7T2vDVcAB0li6BDKZFObsQXdWr6GGKQSUxdQwlPwmKdpBvYR
---

python -m pip install --upgrade pip
pip install numpy==1.23.4
pip install requests
pip install nltk
pip install pyttsx3
pip install moviepy
pip install imageio[ffmpeg] 


 pip install --no-cache-dir --force-reinstall moviepy

pip install moviepy==1.0.3


python -c "import moviepy.editor; print('MoviePy imported successfully')"  --> Checking


pip install google-search-results

pip install mjml   -->  Newsletter template

---

git clone https://github.com/OpenTalker/SadTalker.git
cd SadTalker

pip install scikit-image --prefer-binary

pip install --upgrade pip setuptools wheel

pip install --no-cache-dir --force-reinstall scikit-image


# Install required dependencies
pip install -r requirements.txt

If it is not working

Install miniconda for windows

conda install -c conda-forge conda-libmamba-solver
pip install --no-cache-dir scikit-image
python -c "import skimage; print(skimage.__version__)"

 pip install torch torchvision torchaudio

 pip install opencv-python
 pip install safetensors
 pip install numpy==1.23.5
 pip install kornia
 pip install facexlib
 pip install yacs
 pip install pydub
 pip install gfpgan

 pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.1 -f https://download.pytorch.org/whl/torch_stable.html

pip install pyttsx3
