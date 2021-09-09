import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


app = Flask(__name__)
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
    index = {}
    tem = 0
    probability = [.1,.1,.2,.6]
    x = ['Tatpurush','Dvand',"Bahubrihi","Avyayibhav"]
    # plt.bar(x,probability)
    # plt.xlabel('Compound type')
    # plt.ylabel('Probability')
    # plt.title('Graphical analysis')
    # plt.savefig('static/compo.png')
    filename = 'compo.png'
    compound_type = "Avyayibhav"
    color= ["#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A","#B4E8FC","#FFA9B8","#D1CAFF","#9EFFD6","#F74C4A"]
    for i, word in enumerate(words):
        if '-' in word:
            index[i] = [word, compound_type, filename, 1, color[i]]
            tem += 1
        else:
            index[i] = [word, 'no-compound', filename, 0, color[i]]
    print(index)
    if tem == 0:
        index["empty"] = "No compound word found. Please enter the compund word with '-' in your text."
    
    
    return render_template('index.html', prediction_text = output, index = index)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename= filename), code=301)

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port = 5000)