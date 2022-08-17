# Video Editing
# pip install moviepy
from moviepy.editor import *
import os
import random
allVideos = []

videos = []

for filename in os.listdir("clips"):
  clip = VideoFileClip('clips/'+filename)
  clip = clip.resize(width=1920)
  clip = clip.resize(height=1080)
  clip.set_duration(5)
  allVideos.append(clip)

random.shuffle(allVideos)

for clip in allVideos:
  videos.append(clip)


finalClip = concatenate_videoclips(videos, method="compose")

finalClip.write_videofile('output/test.mp4')

# finalClip.write_videofile('output/test.mp4', threads=8,remove_temp=True, codec="libx264", audio_codec="aac")
# clip_1 = VideoFileClip("clips/img-1.gif")
# clip_2 = VideoFileClip("clips/img-12.gif")
# final_clip = concatenate_videoclips([clip_1, clip_2])
# final_clip.write_videofile("output/output_trimmed.mp4")
# # Adding VFX
# clip_1 = (VideoFileClip("sample_video.mp4").subclip(40, 50).fx(vfx.colorx, 1.2).fx(vfx.lum_contrast, 0, 30, 100))
# clip_2 = (VideoFileClip("sample_video.mp4").subclip(68, 91).fx(vfx.invert_colors))
# final_clip = concatenate_videoclips([clip_1, clip_2])
# final_clip.write_videofile("output_VFX.mp4")
# # Add Audio to Video
# clip = VideoFileClip("sample_video.mp4")
# # Add audio to only first 5 sec
# clip = clip.subclip(0, 5)
# audioclip = AudioFileClip("audio.mp3").subclip(0, 5)
# videoclip = clip.set_audio(audioclip)
# final_clip.write_videofile("output_audio.mp4")