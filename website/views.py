from flask import Blueprint, render_template, request, session, url_for,redirect
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
            yt_url=YouTube(session['link'] )
            yt_url.check_availability()
        except:
            return render_template("error.html")
        return render_template("download.html", yt_url=yt_url)
    
    return render_template("home.html")

