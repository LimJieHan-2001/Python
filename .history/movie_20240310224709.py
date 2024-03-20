import movie.py.editor as mp
video = mp.VideoFileClip(r"sample.mp4")
video.audio.write_audiofile(r"sample.mp3")