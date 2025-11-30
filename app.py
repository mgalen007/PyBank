from flask import Flask, render_template, request
import time



app = Flask(__name__)
current_year = time.localtime().tm_year
host = '127.0.0.1'
port = 8080

@app.route('/')
def login():
    return render_template('login.html', failed_msg='')

@app.route('/auth', methods=['POST'])
def auth():
    users = []
    passwords = []
    with open('data/users.txt', 'r') as users_file, open('data/passwords.txt') as passwords_file:
        users = [user.strip() for user in users_file]
        print(users)
        passwords = [password.strip() for password in passwords_file]
        print(passwords)

    username = request.form['username']
    password = request.form['password']

    if username in users:
        index = users.index(username)
        if passwords[index] == password:
            return render_template('index.html', username=username, current_year=time.localtime().tm_year)
        else:
            return render_template('login.html', error_msg='Invalid username or password!')
    else:
        return render_template('login.html', error_msg='Invalid username or password!')
       
    
@app.route('/login')
def signed_out():
    return render_template('login.html', failed_msg='')

@app.route('/account')
def show_account():
    owner = request.form['username']
    return render_template('account.html', owner=owner , creation_date='', account_type='', current_balance='')

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)

