from flask import Flask, render_template
import requests
import time



app = Flask(__name__)
current_year = time.localtime().tm_year
host = '127.0.0.1'
port = 8080

@app.route('/home')
def home():
    return render_template('index.html', username='Admin', year=current_year)

app.run(host, port)