from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """returns the message welcome"""
    return 'welcome'

@app.route('/welcome/<msg>')
def welcome_msg(msg):
    """returns the message welcome with the msg string in the url"""
    return f"welcome {msg}"
