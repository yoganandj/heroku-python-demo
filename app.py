from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'ItIsASecret'


@app.route('/hello')
def index():
    flash('What is your name')
    return render_template("index.html")


@app.route('/')
@app.route('/home')
def home():
    return "Hello World"


@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('Hi '+str(request.form['name_input']) + ' Good to see you!')
    return render_template("index.html")
