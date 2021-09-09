import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = [x for x in request.form.values()]
    print(text)
    # prediction = model.predict(text)

    output = text[1].strip()
    trans_scheme = text[0]
    len_words = len(output)
    words = output.split(" ")
    num_of_words = len(words)
    index = {}
    tem = 0
    probability = [.1, .1, .2, .6]
    x = ['Tatpurush', 'Dvand', "Bahubrihi", "Avyayibhav"]
    # plt.bar(x,probability)
    # plt.xlabel('Compound type')
    # plt.ylabel('Probability')
    # plt.title('Graphical analysis')
    # plt.savefig('static/compo.png')

    # tags word wise
    tags_word = {0: ["m. sg. g.",  "n. sg. g."], 1: ["pfp. [1]", "f. sg. nom.", "ca. pfp. [1]"], 2: ["f. sg. nom."], 3: ["n. sg. g.", "m. sg. g."], 4: [
        "m. sg. nom."], 5: ["m. sg. nom.", "n. sg. g.", "n. sg. abl."], 6: ["conj."], 7: ["m. sg. i.", "n. sg. i."], 8: ["adv.", "prep."], 9: ["n. sg. acc.", "n. sg. nom."], 10: ["tasil"]}

    # colors that we use
    color = ["#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A", "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A", "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A", "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A",
             "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A", "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A", "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A", "#B4E8FC", "#FFA9B8", "#D1CAFF", "#9EFFD6", "#F74C4A"]

    # recommendation by first model
    other_tags_recommendation = {0: [[0, "m. sg. g.", "#B4E8FC"], [1, "n. sg. g.", "#FFA9B8"]], 1: [[0, "pfp. [1]", "#B4E8FC"], [1, "f. sg. nom.", "#FFA9B8"], [2, "ca. pfp. [1]", "#D1CAFF"]], 2: [[0, "f. sg. nom.", "#B4E8FC"]], 3: [[0, "n. sg. g.", "#B4E8FC"], [1, "m. sg. g.", "#FFA9B8"]], 4: [
        [0, "m. sg. nom.", "#B4E8FC"]], 5: [[0, "m. sg. nom.", "#B4E8FC"], [1, "n. sg. g.", "#FFA9B8"], [2, "n. sg. abl.", "#D1CAFF"]], 6: [[0, "conj.", "#B4E8FC"]], 7: [[0, "m. sg. i.", "#B4E8FC"], [1, "n. sg. i.", "#FFA9B8"]], 8: [[0, "adv.", "#B4E8FC"], [1, "prep.", "#FFA9B8"]], 9: [[0, "n. sg. acc.", "#B4E8FC"], [1, "n. sg. nom.", "#FFA9B8"]], 10: [[0, "tasil", "#B4E8FC"]]}

    # single recommendation by second model
    tag_type = ["n. sg. g.", "f. sg. nom.", "f. sg. nom.", "m. sg. g.", "m. sg. nom.",
                "n. sg. abl.", "conj.", "n. sg. i.", "adv.", "n. sg. nom.", "tasil"]

    # total tags that we have
    total_tags = ["adv.", "prep.", "tasil", "m. sg. i.", "n. sg. i.", "conj.", "m. sg. nom.",
                  "n. sg. g.", "n. sg. abl.", "m. sg. g.", "f. sg. nom.", "pfp. [1]", "ca. pfp. [1]"]

    # tags out of total tags which are not recommended for particular word
    left_tags = {}
    for i in range(num_of_words):
        temp = []
        for j in total_tags:
            if j not in tags_word[i]:
                temp.append(j)
        left_tags[i] = temp

    for i, word in enumerate(words):
        index[i] = [word, tag_type[i], color[i], other_tags_recommendation[i], left_tags[i]]
    print(index)
    if len_words == 0:
        index["empty"] = "You have entered empty sentence. Please enter some text in your sentence."

    return render_template('index.html', prediction_text=output, index=index, total_tags=total_tags)


@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename=filename), code=301)


@app.route('/results', methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port = 4000)
