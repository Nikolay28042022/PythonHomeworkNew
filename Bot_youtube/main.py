"""Pytube."""
import pytube

vidio_link = r'https://www.youtube.com/watch?v=dsLk_rW0dZs&list=RDdsLk_rW0dZs&start_radio=1'

yt = pytube.YouTube(vidio_link)
streams = yt.streams
video_best = streams.order_by('resolution').desc().first()
audio_best = streams.filter(only_audio=True).desc().first()
path = 'C:/Downloads'
video_best.download(path)
audio_best.download(path)
