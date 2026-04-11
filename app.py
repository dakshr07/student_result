from flask import Flask, request, render_template

app = Flask(__name__)

# ================= STUDENT DATA =================
students = {

    "4MH24CI022": {
        "password": "MIT123",
        "name": "Likitha",
        "father": "T S Udaya",
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
        "father": "Ramesh",
        "branch": "ECE",
        "sgpa": "7.32",
        "subjects": [
            {"code": "M23EC301", "name": "Signals & Systems", "cie": 45, "see": 40, "total": 85, "gp": 9, "grade": "A+", "credits": 3},
            {"code": "M23EC302", "name": "Digital Electronics", "cie": 40, "see": 30, "total": 70, "gp": 8, "grade": "A", "credits": 3},
            {"code": "M23EC303", "name": "Network Theory", "cie": 38, "see": 28, "total": 66, "gp": 7, "grade": "B+", "credits": 4},
            {"code": "M23EC304", "name": "Control Systems", "cie": 35, "see": 25, "total": 60, "gp": 6, "grade": "B", "credits": 3},
            {"code": "M23EC305", "name": "Microcontrollers", "cie": 42, "see": 32, "total": 74, "gp": 8, "grade": "A", "credits": 3},
            {"code": "M23ECL306", "name": "ECE Lab", "cie": 44, "see": 46, "total": 90, "gp": 10, "grade": "O", "credits": 2}
        ]
    },

    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi K L",
        "father": "Lokesh",
        "branch": "CSE",
        "sgpa": "7.09",
        "subjects": [
            {"code": "M23CS301", "name": "Data Structures", "cie": 40, "see": 35, "total": 75, "gp": 8, "grade": "A", "credits": 4},
            {"code": "M23CS302", "name": "Operating System", "cie": 38, "see": 28, "total": 66, "gp": 7, "grade": "B+", "credits": 4},
            {"code": "M23CS303", "name": "DBMS", "cie": 42, "see": 30, "total": 72, "gp": 8, "grade": "A", "credits": 3},
            {"code": "M23CS304", "name": "Computer Networks", "cie": 36, "see": 24, "total": 60, "gp": 6, "grade": "B", "credits": 3},
            {"code": "M23CS305", "name": "Software Engineering", "cie": 41, "see": 29, "total": 70, "gp": 8, "grade": "A", "credits": 3},
            {"code": "M23CSL306", "name": "CS Lab", "cie": 45, "see": 47, "total": 92, "gp": 10, "grade": "O", "credits": 2}
        ]
    },

    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "father": "Krishnappa B L",
        "branch": "CSE (AI)",
        "sgpa": "7.65",
        "subjects": [
            {"code": "M23AI301", "name": "Machine Learning", "cie": 45, "see": 35, "total": 80, "gp": 9, "grade": "A+", "credits": 4},
            {"code": "M23AI302", "name": "Data Science", "cie": 42, "see": 30, "total": 72, "gp": 8, "grade": "A", "credits": 3},
            {"code": "M23AI303", "name": "Python Programming", "cie": 48, "see": 40, "total": 88, "gp": 10, "grade": "O", "credits": 3},
            {"code": "M23AI304", "name": "Deep Learning", "cie": 39, "see": 28, "total": 67, "gp": 7, "grade": "B+", "credits": 3},
            {"code": "M23AI305", "name": "AI Lab", "cie": 50, "see": 45, "total": 95, "gp": 10, "grade": "O", "credits": 2}
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
        return render_template("result.html", student=students[usn], usn=usn)
    else:
        return "Invalid USN or Password"

if __name__ == '__main__':
    app.run()
