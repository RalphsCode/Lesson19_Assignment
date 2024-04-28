"""
In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:
/welcome   Returns “welcome”
/welcome/home   Returns “welcome home”
/welcome/back   Return “welcome back”
Once you’ve finished this, run the tests for it:
$python3 -m unittest test.py
"""

from flask import Flask

app = Flask(__name__)  # creating an instance of the Flask Class

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def home():
    return 'welcome home'

@app.route('/welcome/back')
def back():
    return 'welcome back'