import os
import json
from datetime import datetime
from moviepy.editor import (ImageClip, AudioFileClip, concatenate_videoclips, 
                            TextClip, CompositeVideoClip, ColorClip)

def create_video(image_paths, audio_path, subtitle_data_path, output_video_path):
    if not image_paths:
        print("❌ Error: No images found for video creation.")
        return

    if not os.path.exists(audio_path):
        print("❌ Narration file missing! Exiting...")
        return

    audio_clip = AudioFileClip(audio_path)
    total_duration = audio_clip.duration
    image_duration = total_duration / len(image_paths)

    # Improved background creation with a softer color
    background = ColorClip(size=(1280, 720), color=(240, 240, 240)).set_duration(20)

    # Avatar (news reader) resized and positioned centrally on the left side
    avatar_path = "media/avatar.png"
    if not os.path.exists(avatar_path):
        print("❌ Avatar image not found! Exiting...")
        return

    avatar_clip = ImageClip(avatar_path).set_duration(20).resize(height=450).set_position((80, 'center'))

    # Weather images resized and placed at the top-right above the center with improved alignment
    image_clips = []
    for idx, img in enumerate(image_paths):
        try:
            weather_clip = (ImageClip(img)
                            .set_duration(image_duration)
                            .resize(height=150)
                            .set_position(('right', 'center')))
            image_clips.append(weather_clip)
        except Exception as e:
            print(f"❌ Error adding image {img}: {e}")

    if not image_clips:
        print("❌ No valid image clips created.")
        return

    combined_clip = concatenate_videoclips(image_clips, method="compose")

    # Generate subtitles
    subtitle_clips = []
    if os.path.exists(subtitle_data_path):
        with open(subtitle_data_path, 'r') as file:
            subtitle_data = json.load(file)

        for entry in subtitle_data:
            subtitle_clip = (
                TextClip(entry["text"], fontsize=32, color='white', bg_color='#20232a')
                .set_position(('center', 'bottom'))
                .set_start(entry["start"])
                .set_duration(entry["duration"])
            )
            subtitle_clips.append(subtitle_clip)

    # Combine video layers
    final_video = CompositeVideoClip(
        [background, avatar_clip, combined_clip] + subtitle_clips
    ).set_audio(audio_clip)

    # Save final video
    print(f"🔹 Saving video to {output_video_path}...")
    final_video.write_videofile(output_video_path, fps=24)
    print(f"✅ Vlog created successfully: {output_video_path}")

def main():
    today_date = datetime.today().strftime("%Y-%m-%d")
    image_dir = f"media/images/{today_date}"

    if not os.path.exists(image_dir):
        print(f"❌ Error: Image folder for {today_date} not found.")
        return

    image_paths = [
        os.path.join(image_dir, img)
        for img in sorted(os.listdir(image_dir))
        if img.lower().endswith(('.jpg', '.png'))
    ]

    audio_path = "media/narration.mp3"
    subtitle_data_path = "media/subtitles.json"
    output_video_path = "media/output.mp4"

    create_video(image_paths, audio_path, subtitle_data_path, output_video_path)

if __name__ == "__main__":
    main()
