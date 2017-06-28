# Imports for flask
from flask import Blueprint, render_template, url_for, request, flash, redirect
# Imports for handeling sessions
from flask import session as login_session

mod = Blueprint('site', __name__, template_folder='templates')

# We import the controllers
from controller import *

# HANDLERS FOR LANDING PAGES ---------------------------------------------------

print "site package loaded"

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/about')
def aboutus():
    return render_template('about.html')

@mod.route('/contact', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        name = request.form['name']
        q = request.form['about']

        print "%s asked a question" % name
        print "Question is: %s" % q
        return render_template('submitted.html')
    else:
        return render_template('contact.html')
