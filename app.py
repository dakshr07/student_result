from flask import Flask, request, render_template

app = Flask(__name__)

# Student data
students = {
    "4MH24CI022": {
        "password": "MIT123",
        "name": "Likitha",
        "branch": "CSE (AI & ML)",
        "sgpa": "7.15"
    },
    "4MH24EC039": {
        "password": "MIT123",
        "name": "Harshitha C S",
        "branch": "ECE",
        "sgpa": "7.32"
    },
    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi K L",
        "branch": "CSE",
        "sgpa": "7.09"
    },
    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "branch": "CSE (AI)",
        "sgpa": "7.65"
    }
}

@app.route('/')
def home():
    return '<h2>MITM Results</h2><a href="/login">CLICK HERE TO LOGIN</a>'

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/result', methods=['POST'])
def result():
    usn = request.form['usn']
    password = request.form['password']

    if usn in students and students[usn]["password"] == password:
        return render_template("result.html", student=students[usn], usn=usn)
    else:
        return "Invalid USN or Password"

app.run(host='0.0.0.0', port=10000)
