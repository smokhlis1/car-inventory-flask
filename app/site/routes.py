from flask import Blueprint, render_template # type: ignore

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    return render_template('home.html')

@home.route('/profile')
def profile():
    return render_template('profile.html')