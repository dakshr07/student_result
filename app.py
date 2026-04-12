from flask import Flask, request, render_template

app = Flask(__name__)

students = {

    "4MH24CI022": {
        "password": "MIT123",
        "name": "Likitha",
        "branch": "COMPUTER SCIENCE AND ENGINEERING(AI & ML)",
        "father": "Uday T S",
        "sgpa": "7.15",
        "subjects": [
            {"code":"M23BBIOK301","name":"BIOLOGY FOR ENGINEERS","cie":47,"see":41,"total":88,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":41,"see":26,"total":67,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":38,"see":29,"total":67,"gp":7,"grade":"B+","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":36,"see":18,"total":54,"gp":5,"grade":"C","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":42,"see":30,"total":72,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":41,"see":18,"total":59,"gp":6,"grade":"B","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":50,"see":38,"total":88,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":42,"see":45,"total":87,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BPEK310","name":"PHYSICAL EDUCATION","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
        ]
    },

    "4MH24EC039": {
        "password": "MIT123",
        "name": "Harshitha C S",
        "branch": "ELECTRONICS AND COMMUNICATION ENGINEERING",
        "father": "Ramesh C S",
        "sgpa": "7.32",
        "subjects": [
            {"code":"M23BBIOK301","name":"NETWORK ANALYSIS","cie":30,"see":28,"total":58,"gp":8,"grade":"B","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"ANALOG ELECTRONIC CIRCUIT DESIGN","cie":39,"see":21,"total":60,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"DIGITAL SYSTEM DESIGN USING VERILOG","cie":47,"see":30,"total":77,"gp":8,"grade":"A","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"C++ AND DATA STRUCTURE","cie":38,"see":25,"total":63,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"8051 MICROCONTROLLER","cie":37,"see":32,"total":69,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"MICROCONTROLLER LABORATORY","cie":49,"see":25,"total":74,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"ANALOG & DIGITAL SYSTEM DESIGN LABORATORY","cie":45,"see":41,"total":86,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"MATHEMATICS FOR ECE STREAM","cie":40,"see":28,"total":68,"gp":7,"grade":"B+","credits_reg":1,"credits_earned":1},
            {"code":"M23BPEK310","name":"NATIONAL SERVICE SCHEME(NSS)","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
        ]
    },

    "4MH24CS075": {
        "password": "MIT123",
        "name": "Kushi KAVERAMMA L",
        "branch": "COMPUTER SCIENCE AND ENGINEERING",
        "father": "Lokesh K",
        "sgpa": "7.09",
        "subjects": [
            
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":37,"see":21,"total":58,"gp":6,"grade":"B","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":45,"see":23,"total":68,"gp":7,"grade":"B+","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":42,"see":31,"total":73,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":39,"see":18,"total":57,"gp":6,"grade":"B","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":38,"see":26,"total":64,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":49,"see":46,"total":95,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":45,"see":38,"total":83,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BBIOK301","name":"MATHEMATICS","cie":41,"see":18,"total":59,"gp":6,"grade":"B","credits_reg":3,"credits_earned":3},
            {"code":"M23BPEK310","name":"YOGA","cie":100,"see":0,"total":100,"gp":0,"grade":"PP","credits_reg":0,"credits_earned":0},
            {"code":"M23BSCK308","name":"SOCIAL CONNECT AND RESPONSIBILITY","cie":100,"see":0,"total":100,"gp":10,"grade":"O","credits_reg":1,"credits_earned":1}
        ]
    },

    "4MH24CA056": {
        "password": "MIT123",
        "name": "Tejaswini B K",
        "branch": "COMPUTER SCIENCE AND ENGINEERING (AI)",
        "father": "Krishnappa B L",
        "sgpa": "7.65",
        "subjects": [
            {"code":"M23BBIOK301","name":"BIOLOGY FOR ENGINEERS","cie":50,"see":47,"total":97,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCS302","name":"LOGIC DESIGN AND COMPUTER ORGANIZATION","cie":47,"see":30,"total":77,"gp":8,"grade":"A","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS303","name":"OPERATING SYSTEM","cie":44,"see":23,"total":67,"gp":7,"grade":"B+","credits_reg":4,"credits_earned":4},
            {"code":"M23BCS304","name":"DATA STRUCTURES AND APPLICATIONS","cie":43,"see":18,"total":61,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS305","name":"SOFTWARE ENGINEERING","cie":42,"see":22,"total":64,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS306B","name":"OOPS WITH JAVA","cie":40,"see":21,"total":61,"gp":7,"grade":"B+","credits_reg":3,"credits_earned":3},
            {"code":"M23BCS309A","name":"DATA VISUALIZATION WITH PYTHON","cie":49,"see":33,"total":82,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
            {"code":"M23BCSL307","name":"DATA STRUCTURES LAB","cie":45,"see":36,"total":81,"gp":9,"grade":"A+","credits_reg":1,"credits_earned":1},
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
