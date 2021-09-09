from flaskext.markdown import Markdown
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# importing custom module named as scrap
import scrap


app = Flask(__name__)
Markdown(app)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    text = [x for x in request.form.values()]
    print(text)
    # prediction = model.predict(text)

    output = text[1]
    trans_scheme = text[0]
    words = output.split(" ")
    html = scrap.scrap_html(words)
    # print(html) 
    
    return render_template('index.html', result = html)

if __name__ == "__main__":
    app.run(debug=True)