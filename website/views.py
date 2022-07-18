from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if(request.method == 'POST'):
        yt_url = request.form.get('yt_url')
        
    return render_template("base.html")