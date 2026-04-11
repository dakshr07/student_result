from flask import Flask, request, render_template

app = Flask(__name__)

# ================= COMMON SUBJECTS =================
common_subjects = [
    {"code": "M23BBIOK301", "name": "BIOLOGY FOR ENGINEERS", "credits": 1},
    {"code": "M23BCS302", "name": "LOGIC DESIGN AND COMPUTER ORGANIZATION", "credits": 3},
    {"code": "M23BCS303", "name": "OPERATING SYSTEM", "credits": 4},
    {"code": "M23BCS304", "name": "DATA STRUCTURES AND APPLICATIONS", "credits": 3},
    {"code": "M23BCS305", "name": "SOFTWARE ENGINEERING", "credits": 3},
    {"code": "M23BCS306B", "name": "OOPS WITH JAVA", "credits": 3},
    {"code": "M23BCS309A", "name": "DATA VISUALIZATION WITH PYTHON", "credits": 1},
    {"code": "M23BCSL307", "name": "DATA STRUCTURES LAB", "credits": 1},
    {"code": "M23BPEK310", "name": "PHYSICAL EDUCATION (PE)", "credits": 0},
    {"code": "M23BSCK308", "name": "SOCIAL CONNECT AND RESPONSIBILITY", "credits": 1}
]

# ================= STUDENTS =================
students = {

    "4MH24CI022": {
        "password": "MIT123",
        "name": "Likitha",
        "father": "Uday T S",
        "branch": "CSE (AI & ML)",
        "sgpa": "8.50",
        "marks": [
            [49,44,"O"],
            [44,29,"A"],
            [43,42,"A+"],
            [48,39,"A+"],
            [47,25,"A"],
            [42,26,"B+"],
            [44,47,"O"],
            [43,35,"A"],
            [100,0,"PP"],
            [100,0,"O"]
        ]
    },

    "4MH24EC039": {
        "password": "MIT123",
        "name": "Harshitha C S",
        "father": "Ramesh",
        "branch": "ECE",
        "sgpa": "7.80",
        "marks": [
            [45,40,"A+"],
            [40,28,"A"],
            [38,30,"B+"],
            [35,25,"B"],
            [42,30,"A"],
            [40,20,"B"],
            [48,35,"A+"],
            [40,38,"A"],
            [100,0,"PP"],
            [100,0,"O"]
        ]
    },

    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi K L",
        "father": "Lokesh",
        "branch": "CSE",
        "sgpa": "7.20",
        "marks": [
            [42,38,"A"],
            [39,25,"B+"],
            [35,28,"B"],
            [30,20,"C"],
            [40,30,"A"],
            [38,18,"B"],
            [45,40,"A+"],
            [40,35,"A"],
            [100,0,"PP"],
            [100,0,"O"]
        ]
    },

    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "father": "Krishnappa B L",
        "branch": "CSE (AI)",
        "sgpa": "8.10",
        "marks": [
            [48,42,"O"],
            [42,30,"A"],
            [40,35,"A+"],
            [45,38,"A+"],
            [44,28,"A"],
            [41,20,"B+"],
            [49,45,"O"],
            [42,40,"A+"],
            [100,0,"PP"],
            [100,0,"O"]
        ]
    }

}

# ================= ROUTES =================

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

    if usn in students and students[usn]['password'] == password:
        return render_template("result.html",
                               student=students[usn],
                               usn=usn,
                               subjects=common_subjects)
    else:
        return "Invalid USN or Password"

if __name__ == '__main__':
    app.run()
