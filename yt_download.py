from textwrap import indent
from flask import send_file
from pytube import YouTube
from sys import argv
import pprint

def yt_download(yt_url):

    yt = YouTube(yt_url,allow_oauth_cache=True)

    # print(yt)

    print('Title:', yt.title)

    print('Author:',yt.author)

    print('View:', yt.views)

    # pp = pprint.PrettyPrinter(indent=4)

    # pp.pprint({'Info': yt.vid_info})

    yd = yt.streams.get_lowest_resolution()

    path=yd.download('./yt_downloads')

    fname = path.split('//')[-1]
    return send_file(fname, as_attachment=True)