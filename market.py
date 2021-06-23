from flask import Flask, render_template

app = Flask(__name__)
# start storing html files into a template directory and user 'render_template'
@app.route('/')
def home_page():
    return render_template('home.html')
    


