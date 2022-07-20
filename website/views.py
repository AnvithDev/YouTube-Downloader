from flask import Blueprint, render_template, request
from yt_download import yt_download

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if(request.method == 'POST'):
        yt_url = request.form.get('yt_url')

        yt_download(yt_url)
        
    return render_template("base.html")