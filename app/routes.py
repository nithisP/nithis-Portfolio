from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/home')
def home():
    return render_template('home.html')

@main_bp.route('/education')
def education():
    # If you later want dynamic data, pass context here
    return render_template('education.html')
