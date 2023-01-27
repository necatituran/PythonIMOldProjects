import speech_recognition as sr
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

num_seconds = 52*60
print("The video is {} seconds long".format(num_seconds))
l = list(range(0, num_seconds, 60))

dizionario = {}

for i in range(len(1)-1):
    ffmpeg_extract_subclip(
        "video.mp4", l[i], l[i+1], targetname="video{}.mp4".format(i))
    clip = mp.VideoFileClip("video{}.mp4".format(i))
    clip.audio.write_audiofile("audio{}.wav".format(i))
    r = sr.Recognizer()
    with sr.AudioFile("audio{}.wav".format(i)) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    result = r.recognize_google(audio, language="it-IT")
    dizionario['video{}'.format(i)] = result

l_chunks = [dizionario['chunk{}'.format(i+1)] for i in range(len(dizionario))]
text = '\n'.join(l_chunks)

with open('recognized.txt', mode='w') as file:
    file.write("Recognized Speech:")
    file.write("\n")
    file.write(text)
    print("Finally ready!")
