from io import BytesIO
from flask import Blueprint, render_template, request, send_file, session, url_for,redirect
from textwrap import indent
from pytube import YouTube
from sys import argv
import pprint

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if(request.method == 'POST'):
        session['link'] = request.form.get('yt_url')
        try:
            yt_url=YouTube(session['link'])
            yt_url.check_availability()
        except:
            return render_template("error.html")
        return render_template("download.html", yt_url=yt_url)
    
    return render_template("home.html")

@views.route('/download', methods=['GET','POST'])
def yt_download():
    if request.method=='POST':
        buffer = BytesIO()
        yt_url=YouTube(session['link'],allow_oauth_cache=True)
        itag= request.form.get('itag')
        video = yt_url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        video_download_name = yt_url.title+".mp4"
        return send_file(buffer, as_attachment="True", download_name=video_download_name, mimetype="video/mp4")
    
    return redirect(url_for('home'))