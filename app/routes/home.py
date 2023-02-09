from flask import Blueprint, render_template

<<<<<<< HEAD
bp = Blueprint('home', __name__, url_prefix= '/')

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')
    
=======
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')
>>>>>>> b1b445c355c21ff1b8e66a89bc859fc9f20d67fa
