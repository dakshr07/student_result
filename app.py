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
            {"code": "M23BBIOK301", "name": "Biology for Engineers", "cie": 47, "see": 41, "total": 88, "gp": 9, "grade": "A+", "credits": 1},
            {"code": "M23BCS302", "name": "LDCO", "cie": 41, "see": 26, "total": 67, "gp": 7, "grade": "B+", "credits": 3},
            {"code": "M23BCS303", "name": "Operating System", "cie": 38, "see": 29, "total": 67, "gp": 7, "grade": "B+", "credits": 4},
            {"code": "M23BCS304", "name": "Data Structures", "cie": 36, "see": 18, "total": 54, "gp": 5, "grade": "C", "credits": 3},
            {"code": "M23BCS305", "name": "Software Engineering", "cie": 42, "see": 30, "total": 72, "gp": 8, "grade": "A", "credits": 3},
            {"code": "M23BCS306", "name": "OOPS with Java", "cie": 41, "see": 18, "total": 59, "gp": 6, "grade": "B", "credits": 3},
            {"code": "M23BCS309", "name": "Data Visualization", "cie": 50, "see": 38, "total": 88, "gp": 9, "grade": "A+", "credits": 1},
            {"code": "M23BCSL307", "name": "DS Lab", "cie": 42, "see": 45, "total": 87, "gp": 9, "grade": "A+", "credits": 1}
        ]
    },

    "4MH24EC039": {
        "password": "MIT123",
        "name": "Harshitha C S",
        "branch": "ECE",
        "sgpa": "7.32",
        "subjects": [
            {"code": "EC301", "name": "Signals & Systems", "cie": 45, "see": 40, "total": 85, "gp": 9, "grade": "A+", "credits": 3},
            {"code": "EC302", "name": "Digital Electronics", "cie": 40, "see": 30, "total": 70, "gp": 8, "grade": "A", "credits": 3},
            {"code": "EC303", "name": "Network Theory", "cie": 38, "see": 28, "total": 66, "gp": 7, "grade": "B+", "credits": 4},
            {"code": "EC304", "name": "Control Systems", "cie": 35, "see": 25, "total": 60, "gp": 6, "grade": "B", "credits": 3},
            {"code": "EC305", "name": "Microcontrollers", "cie": 42, "see": 32, "total": 74, "gp": 8, "grade": "A", "credits": 3}
        ]
    },

    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi K L",
        "branch": "CSE",
        "sgpa": "7.09",
        "subjects": [
            {"code": "CS301", "name": "Data Structures", "cie": 40, "see": 35, "total": 75, "gp": 8, "grade": "A", "credits": 4},
            {"code": "CS302", "name": "Operating System", "cie": 38, "see": 28, "total": 66, "gp": 7, "grade": "B+", "credits": 4},
            {"code": "CS303", "name": "DBMS", "cie": 42, "see": 30, "total": 72, "gp": 8, "grade": "A", "credits": 3},
            {"code": "CS304", "name": "Computer Networks", "cie": 36, "see": 24, "total": 60, "gp": 6, "grade": "B", "credits": 3},
            {"code": "CS305", "name": "Software Engineering", "cie": 41, "see": 29, "total": 70, "gp": 8, "grade": "A", "credits": 3}
        ]
    },

    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "branch": "CSE (AI)",
        "sgpa": "7.65",
        "subjects": [
            {"code": "AI301", "name": "Machine Learning", "cie": 45, "see": 35, "total": 80, "gp": 9, "grade": "A+", "credits": 4},
            {"code": "AI302", "name": "Data Science", "cie": 42, "see": 30, "total": 72, "gp": 8, "grade": "A", "credits": 3},
            {"code": "AI303", "name": "Python Programming", "cie": 48, "see": 40, "total": 88, "gp": 10, "grade": "O", "credits": 3},
            {"code": "AI304", "name": "Deep Learning", "cie": 39, "see": 28, "total": 67, "gp": 7, "grade": "B+", "credits": 3},
            {"code": "AI305", "name": "AI Lab", "cie": 50, "see": 45, "total": 95, "gp": 10, "grade": "O", "credits": 2}
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
