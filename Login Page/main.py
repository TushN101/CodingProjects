import json
import re
from flask import Flask, render_template, request, redirect, url_for, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_users():
    with open('users.json') as f:
        return json.load(f)

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)  

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
)

@app.route('/')
def dashboard():
    user_email = session.get('user_email', 'Guest')
    option = ''
    if user_email != 'Guest':
        option = "Logout"
    return render_template("dashboard.html", email=user_email , option=option)

@app.route('/login', methods=['GET','POST'])
@limiter.limit("5 per 30 minuteS", methods=["POST"])
def login():
    if request.method == 'POST': 
        email = request.form['email']
        password = request.form['password']
        users = load_users()
        if users[email]['counter'] < 2:
            if email in users and users[email]['password'] == password: 
                print(f"Successful Login attempt - Email: {email}") 
                users[email]['counter'] = 0
                save_users(users)
                session['user_email'] = email
                return redirect(url_for('dashboard'))
            else:
                error = "Incorrect Username or Password"
                users[email]['counter'] = users[email]['counter'] + 1 
                save_users(users)
                print(f"Failed Login attempt - Email: {email} Password: {password}")  # Log the login attempt
                return render_template('login.html',error=error)
        else:
            error=f"| Account Locked | Contact Admin |"
            return render_template('login.html',error=error)

    return render_template('login.html')

@app.errorhandler(429)
def bad_request(e):
    return render_template("bad_request.html") , 429

@app.route('/recovery', methods=['GET', 'POST'])
def recovery():
    if request.method == 'POST':
        email = request.form['email']
        users = load_users()
        if email in users:
            print(f"Recovery attempt - Email: {email}") 
            return render_template('reset.html', email=email, question=users[email]['secret_question'])
        else:
            error = "Account not found for that Email Address"
            print(f"Failed Recovery attempt - Email: {email}") 
            return render_template('recovery.html',error=error)
    return render_template('recovery.html')

@app.route('/reset', methods=['POST'])
def reset():
    if request.method == 'POST':
        email = request.form['email']  
        answer = request.form['answer']
        new_password = request.form['password']
        users = load_users()
        if email in users and users[email]['secret_answer'] == answer:
            print(f"Reset attempt - Email: {email}") 
            users[email]['password'] = new_password 
            save_users(users)  
            return redirect(url_for('dashboard'))  
        else:
            print(f"Failed Reset attempt - Email: {email}, Answer: {answer}") 
            error = "Authentication Failed | Couldnt Verify User"
            return render_template('reset.html',error=error,email=email,question=users[email]['secret_question']) 


@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect(url_for('dashboard'))


@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("3 per minute", methods=["POST"])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        secret_question = request.form['security_question']
        secret_answer = request.form['security_answer']
        users = load_users() 
        
        if email in users:
            error = "Email-account already exists"
            return render_template("register.html",error=error)
        error=validate_password(password)
        
        if (error!=''):
            return render_template("register.html",error=error)

        users[email] = {
            'password': password,
            'secret_question': secret_question,
            'secret_answer': secret_answer,
            'counter':0
        }
        save_users(users)
        return redirect(url_for('login'))  
    return render_template("register.html")

def validate_password(password):
    if len(password) < 8:
        return "Password should be more than 8 characters"
    if not re.search(r'[A-Z]', password):
        return "Password should contain one capital letter"
    if not re.search(r'[a-z]', password):
        return "Password should contain one small letter"
    if not re.search(r'\d', password):
        return "Password should contain one digit"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain one special character"
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
