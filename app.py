from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>MITM Results</h2><a href="/login">CLICK HERE TO LOGIN</a>'

@app.route('/login')
def login():
    return '''
    <form action="/result" method="post">
    USN: <input name="usn"><br><br>
    Password: <input type="password" name="password"><br><br>
    <button>Result</button>
    </form>
    '''

@app.route('/result', methods=['POST'])
def result():
    usn = request.form['usn']
    password = request.form['password']

    if usn == "4MH24CI022" and password == "MIT123":
        return "Likitha SGPA 7.15"

    elif usn == "4MH24EC039" and password == "MIT123":
        return "Harshitha SGPA 7.32"

    elif usn == "4MH24CS075" and password == "MIT123":
        return "Kushi SGPA 7.09"

    elif usn == "4MH24CA056" and password == "MIT123":
        return "Tejaswini SGPA 7.65"

    else:
        return "Invalid"

app.run(host='0.0.0.0', port=10000)
