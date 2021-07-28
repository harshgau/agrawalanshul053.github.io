import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests

# load the nlp model and tfidf vectorizer from disk
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open('tranform.pkl', 'rb'))


def create_similarity():
    data = pd.read_csv('edited_id.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['1'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data, similarity


def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['1'].unique():
        return('Sorry! The shloka you requested is not in our database. Please check the spelling or try with some other shlokas')
    else:
        i = data.loc[data['1'] == m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        # excluding first item since it is the requested movie itself
        lst = lst[1:11]
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['1'][a])
        return l

# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])


def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', '')
    my_list[-1] = my_list[-1].replace('"]', '')
    return my_list


def get_suggestions():
    data = pd.read_csv('edited_id.csv')
    id = list(data['merged'])
    return id


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template('home.html', suggestions=suggestions)


@app.route("/similarity", methods=["POST"])
def similarity():
    movie = request.form['name']
    rc = rcmd(movie)
    if type(rc) == type('string'):
        return rc
    else:
        m_str = "---".join(rc)
        return m_str


@app.route("/recommend", methods=["POST"])
def recommend():
    Shloka_input = request.form['name']
    Id = 'BG 4.3'
    Shloka = "This the shloka"
    Exact_meaning = "This is the exact meaning"
    Word_Meaning = "this is word meaning"
    Purport = "This is the purport"
    data = pd.read_csv("edited_id.csv")
    Id = data['id'][0]
    Shloka = data['1'][0]
    Exact_meaning = data['5'][0]
    Word_Meaning = data['4'][0]
    Purport = "The topics discussed by Dhṛtarāṣṭra and Sañjaya, as described in the Mahābhārata, form the basic principle for this great philosophy. It is understood that this philosophy evolved on the Battlefield of Kurukṣetra, which is a sacred place of pilgrimage from the immemorial time of the Vedic age. It was spoken by the Lord when He was present personally on this planet for the guidance of mankind."

    casts = {data['id'][i]: [data['0'][i], data['1'][i]]
             for i in range(10)}  # Showing ten custom

    cast_details = {data['id'][i]: [data['0'][i], data['1'][i], data['4'][i],
                                    data['5'][i], data['6'][i][8:]] for i in range(10)}  # we will add another list for Purport

    return render_template('recommend_test.html', Id=Id, Shloka=Shloka, Exact_meaning=Exact_meaning, Word_Meaning=Word_Meaning, Purport=Purport, casts=casts, cast_details=cast_details)


if __name__ == '__main__':
    app.run(debug=True)
