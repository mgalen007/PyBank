from flask import Flask, render_template, request
import time



app = Flask(__name__)
current_year = time.localtime().tm_year
host = '127.0.0.1'
port = 8080

@app.route('/')
def auth():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST': 
        user = request.form['username']
        return render_template('index.html', username=user, year=current_year)
    
@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)

