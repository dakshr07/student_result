from flask import Flask, request, render_template

app = Flask(__name__)

# Student data
students = {

    "4MH24CI022": {
        "password": "MIT123",
        "name": "Likitha",
        "branch": "CSE (AI & ML)",
        "sgpa": "7.15",
        "subjects": [
            {"name": "Biology for Engineers", "cie": 47, "see": 41, "total": 88, "grade": "A+"},
            {"name": "LDCO", "cie": 41, "see": 26, "total": 67, "grade": "B+"},
            {"name": "Operating System", "cie": 38, "see": 29, "total": 67, "grade": "B+"},
            {"name": "Data Structures", "cie": 36, "see": 18, "total": 54, "grade": "C"},
            {"name": "Software Engineering", "cie": 42, "see": 30, "total": 72, "grade": "A"},
            {"name": "OOPS with Java", "cie": 41, "see": 18, "total": 59, "grade": "B"},
            {"name": "Data Visualization", "cie": 50, "see": 38, "total": 88, "grade": "A+"},
            {"name": "DS Lab", "cie": 42, "see": 45, "total": 87, "grade": "A+"}
        ]
    },

    "4MH24EC039": {
        "password": "MIT123",
        "name": "Harshitha C S",
        "branch": "ECE",
        "sgpa": "7.32",
        "subjects": [
            {"name": "Maths", "cie": 45, "see": 40, "total": 85, "grade": "A+"},
            {"name": "Electronics", "cie": 40, "see": 30, "total": 70, "grade": "A"},
            {"name": "Signals", "cie": 38, "see": 28, "total": 66, "grade": "B+"},
            {"name": "Networks", "cie": 35, "see": 25, "total": 60, "grade": "B"},
            {"name": "Microprocessor", "cie": 42, "see": 32, "total": 74, "grade": "A"},
            {"name": "Lab 1", "cie": 44, "see": 46, "total": 90, "grade": "A+"}
        ]
    },

    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi K L",
        "branch": "CSE",
        "sgpa": "7.09",
        "subjects": [
            {"name": "Maths", "cie": 40, "see": 35, "total": 75, "grade": "A"},
            {"name": "C Programming", "cie": 38, "see": 30, "total": 68, "grade": "B+"},
            {"name": "Python", "cie": 42, "see": 36, "total": 78, "grade": "A"},
            {"name": "DS", "cie": 35, "see": 25, "total": 60, "grade": "B"},
            {"name": "DBMS", "cie": 39, "see": 29, "total": 68, "grade": "B+"},
            {"name": "Lab", "cie": 45, "see": 47, "total": 92, "grade": "A+"}
        ]
    },

    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "branch": "CSE (AI)",
        "sgpa": "7.65",
        "subjects": [
            {"name": "AI", "cie": 48, "see": 40, "total": 88, "grade": "A+"},
            {"name": "ML", "cie": 45, "see": 35, "total": 80, "grade": "A+"},
            {"name": "Python", "cie": 42, "see": 30, "total": 72, "grade": "A"},
            {"name": "Data Science", "cie": 40, "see": 28, "total": 68, "grade": "B+"},
            {"name": "Statistics", "cie": 38, "see": 26, "total": 64, "grade": "B+"},
            {"name": "Lab", "cie": 46, "see": 48, "total": 94, "grade": "A+"}
        ]
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
