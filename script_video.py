import os
import random
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):
        img = os.path.join(folder, filename)
        if os.path.isfile(img):
            images.append(img)
    return images

def resize_image(image_path, target_size=(1920, 1080)):
    image = ImageClip(image_path)
    original_size = image.size
    width, height = original_size
    
    if width / height < target_size[0] / target_size[1]:
        new_height = int(height * target_size[0] / width)
        new_width = target_size[0]
    else:
        new_width = int(width * target_size[1] / height)
        new_height = target_size[1]
    
    resized_image = image.resize((new_width, new_height))
    return resized_image

def apply_effect(image, effect, duration=3.5):
    if effect == "zoom_in":
        return image.fx(vfx.resize, lambda t: 1 + 0.2 * t).set_duration(duration)
    elif effect == "zoom_out":
        return image.fx(vfx.resize, lambda t: 1 - 0.1 * t).set_duration(duration)
    elif effect == "shake_zoom_in_little":
        return (
            image.fx(vfx.resize, lambda t: 1 + 0.15 * t)
                .fx(vfx.rotate, lambda t: 3 * t if t < duration / 2 else 3 * (duration - t))
                .set_duration(duration)
        )
    elif effect == "zoom_in_slowly":
        return image.fx(vfx.resize, lambda t: 1 + 0.05 * t).set_duration(duration)
    elif effect == "zoom_in_slowly_shake":
        return (
            image.fx(vfx.resize, lambda t: 1 + 0.05 * t)
                .fx(vfx.rotate, lambda t: 2 * t if t < duration / 2 else 2 * (duration - t))
                .set_duration(duration)
        )
    elif effect == "shake_fast_zoom_in":
        return (
            image.fx(vfx.resize, lambda t: 1 + 0.3 * t)
                .fx(vfx.rotate, lambda t: 3 * t if t < duration / 2 else 3 * (duration - t))
                .set_duration(duration)
        )
    
def add_padding(video, target_size=(1080, 1920)):
    original_size = video.size
    width, height = original_size
    
    if width / height < target_size[0] / target_size[1]:
        new_width = target_size[0]
        new_height = int(height * target_size[0] / width)
    else:
        new_height = target_size[1]
        new_width = int(width * target_size[1] / height)
    
    background = ColorClip(size=target_size, color=(0, 0, 0))
    padded_video = CompositeVideoClip([video.set_position(("center", "center"))], size=target_size)
    return padded_video

def generate_subtitles(subtitle_file, video_duration, video_size):
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=65, color='white', size=video_size, method='caption').set_position(('center', 'bottom'))
    subtitles = SubtitlesClip(subtitle_file, generator)
    return subtitles.set_duration(video_duration)

def create_video(image_folder, audio_file, subtitle_file, output):
    images = load_images_from_folder(image_folder)
    video_clips = []
    effects = ["zoom_in", "zoom_out", "shake_zoom_in_little", "zoom_in_slowly", "zoom_in_slowly_shake", "shake_fast_zoom_in"]

    for i, img_path in enumerate(images):
        image = resize_image(img_path).set_duration(3.5)
        if i == 0:
            video_clip = apply_effect(image, "zoom_in")
        elif i == 1:
            video_clip = apply_effect(image, "zoom_out")
        else:
            effect = random.choice(effects)
            video_clip = apply_effect(image, effect)
        video_clips.append(video_clip)

    video = concatenate_videoclips(video_clips, method="compose")
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    padded_video = add_padding(video)

    subtitles = generate_subtitles(subtitle_file, video.duration, padded_video.size)
    final_video = CompositeVideoClip([padded_video, subtitles])
    
    final_video.write_videofile(output, fps=24)

# Paths to image folder, audio file, subtitle file, and output video file
image_folder = 'images4'
audio_file = 'test6-output.mp3'
subtitle_file = 'test6-output.mp3_en-US.srt'
output_file = 'output_video_with_subtitles.mp4'

create_video(image_folder, audio_file, subtitle_file, output_file)