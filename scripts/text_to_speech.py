import os
import pyttsx3
import json

def text_to_speech(audio_path, subtitle_path):
    script_path = "data/vlog_script.txt"

    if not os.path.exists(script_path):
        print(f"❌ Error: The file {script_path} does not exist.")
        return

    with open(script_path, "r", encoding="utf-8") as file:
        script = file.read().strip()

    if not script:
        print("❌ Error: The script file is empty.")
        return

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Speed
    engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    # Generate subtitles with timestamps
    words = script.split()
    subtitle_data = []
    time_per_word = 0.5  # Assume each word takes 0.5 seconds
    start_time = 0.0

    for word in words:
        subtitle_data.append({
            "text": word,
            "start": round(start_time, 2),
            "duration": round(time_per_word, 2)
        })
        start_time += time_per_word

    # Save the generated subtitle file
    with open(subtitle_path, 'w', encoding='utf-8') as subtitle_file:
        json.dump(subtitle_data, subtitle_file, indent=4)

    # Save narration to audio file
    engine.save_to_file(script, audio_path)
    engine.runAndWait()

    print(f"✅ Narration saved as {audio_path}")
    print(f"✅ Subtitles saved as {subtitle_path}")

if __name__ == "__main__":
    text_to_speech("media/narration.mp3", "media/subtitles.json")
