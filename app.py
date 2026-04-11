from flask import Flask, request, render_template

app = Flask(__name__)

students = {

    "4MH24CI022": {
        "password": "MIT123",
        "name": "Likitha",
        "branch": "CSE (AI & ML)",
        "father": "Uday T S",
        "sgpa": "8.50",
        "subjects": [
            {"code":"M23BBIOK301","name":"BIOLOGY FOR ENGINEERS","cie":49,"see":44,"total":93,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":44,"see":29,"total":73,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":43,"see":42,"total":85,"gp":9,"grade":"A+","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":48,"see":39,"total":87,"gp":9,"grade":"A+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":47,"see":25,"total":72,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":42,"see":26,"total":68,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":44,"see":47,"total":91,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":43,"see":35,"total":78,"gp":8,"grade":"A","credits_reg":1,"credits_earned":1},
            {"code":"M23BPEK310","name":"PHYSICAL EDUCATION","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
        ]
    },

    "4MH24EC039": {
        "password": "MIT123",
        "name": "Harshitha C S",
        "branch": "ECE",
        "father": "Ramesh C S",
        "sgpa": "7.90",
        "subjects": [
            {"code":"M23BBIOK301","name":"BIOLOGY FOR ENGINEERS","cie":45,"see":40,"total":85,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":40,"see":25,"total":65,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":38,"see":30,"total":68,"gp":7,"grade":"B+","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":42,"see":35,"total":77,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":40,"see":28,"total":68,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":39,"see":27,"total":66,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":46,"see":40,"total":86,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":40,"see":38,"total":78,"gp":8,"grade":"A","credits_reg":1,"credits_earned":1},
            {"code":"M23BPEK310","name":"PHYSICAL EDUCATION","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
        ]
    },

    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi K L",
        "branch": "CSE",
        "father": "Lokesh K",
        "sgpa": "8.10",
        "subjects": [
            {"code":"M23BBIOK301","name":"BIOLOGY FOR ENGINEERS","cie":48,"see":42,"total":90,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":42,"see":28,"total":70,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":40,"see":35,"total":75,"gp":8,"grade":"A","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":41,"see":33,"total":74,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":44,"see":30,"total":74,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":40,"see":25,"total":65,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":48,"see":45,"total":93,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":45,"see":40,"total":85,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BPEK310","name":"PHYSICAL EDUCATION","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
        ]
    },

    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "branch": "CSE (AI)",
        "father": "Krishnappa B L",
        "sgpa": "7.65",
        "subjects": [
            {"code":"M23BBIOK301","name":"BIOLOGY FOR ENGINEERS","cie":46,"see":41,"total":87,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":39,"see":26,"total":65,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":37,"see":29,"total":66,"gp":7,"grade":"B+","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":36,"see":18,"total":54,"gp":5,"grade":"C","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":42,"see":30,"total":72,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":41,"see":18,"total":59,"gp":6,"grade":"B","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":50,"see":38,"total":88,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":42,"see":45,"total":87,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BPEK310","name":"PHYSICAL EDUCATION","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
