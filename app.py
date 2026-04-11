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
        {"name": "Logic Design", "cie": 41, "see": 26, "total": 67, "grade": "B+"},
        {"name": "Operating System", "cie": 38, "see": 29, "total": 67, "grade": "B+"},
        {"name": "Data Structures", "cie": 36, "see": 18, "total": 54, "grade": "C"},
        {"name": "Software Engineering", "cie": 42, "see": 30, "total": 72, "grade": "A"}
    ]
}
    },
    "4MH24EC039": {
    "password": "MIT123",
    "name": "Harshitha C S",
    "branch": "ECE",
    "sgpa": "7.32",
    "subjects": [
        {"name": "Biology for Engineers", "cie": 45, "see": 40, "total": 85, "grade": "A"},
        {"name": "Logic Design", "cie": 40, "see": 28, "total": 68, "grade": "B+"},
        {"name": "Operating System", "cie": 39, "see": 30, "total": 69, "grade": "B+"},
        {"name": "Data Structures", "cie": 37, "see": 20, "total": 57, "grade": "C"},
        {"name": "Software Engineering", "cie": 43, "see": 31, "total": 74, "grade": "A"}
    ]
},
    },
    "4MH24CS075": {
    "password": "MIT123",
    "name": "Kushi K L",
    "branch": "CSE",
    "sgpa": "7.09",
    "subjects": [
        {"name": "Biology for Engineers", "cie": 46, "see": 39, "total": 85, "grade": "A"},
        {"name": "Logic Design", "cie": 38, "see": 27, "total": 65, "grade": "B"},
        {"name": "Operating System", "cie": 36, "see": 28, "total": 64, "grade": "B"},
        {"name": "Data Structures", "cie": 35, "see": 19, "total": 54, "grade": "C"},
        {"name": "Software Engineering", "cie": 41, "see": 29, "total": 70, "grade": "A"}
    ]
},
    },
    "4MH24CA056": {
    "password": "MIT123",
    "name": "Tejaswini B K",
    "branch": "CSE (AI)",
    "sgpa": "7.65",
    "subjects": [
        {"name": "Biology for Engineers", "cie": 48, "see": 42, "total": 90, "grade": "A+"},
        {"name": "Logic Design", "cie": 42, "see": 30, "total": 72, "grade": "A"},
        {"name": "Operating System", "cie": 40, "see": 32, "total": 72, "grade": "A"},
        {"name": "Data Structures", "cie": 38, "see": 22, "total": 60, "grade": "B"},
        {"name": "Software Engineering", "cie": 44, "see": 34, "total": 78, "grade": "A"}
    ]
}
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
