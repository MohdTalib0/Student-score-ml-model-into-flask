from cProfile import run
from flask import Flask, render_template, redirect, request
import flask
import pickle
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def marks():
    if request.method  == 'POST':
        hours =  float(request.form['input'])
        marks = str(model.predict([[hours]])[0][0])
    return render_template("index.html", your_marks = marks)
if __name__ == '__main__':
    app.run(debug = True)