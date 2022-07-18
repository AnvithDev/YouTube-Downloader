from textwrap import indent
from pytube import YouTube
from sys import argv
import pprint

link = argv[1]

yt = YouTube(link)

print(yt)

print('Title:', yt.title)

print('Author:',yt.author)

print('View:', yt.views)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint({'Info': yt.vid_info})

yd = yt.streams.get_lowest_resolution()

yd.download('./yt_downloads')