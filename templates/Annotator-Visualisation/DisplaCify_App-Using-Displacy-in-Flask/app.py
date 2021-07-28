from flaskext.markdown import Markdown
import Sanskrit
import json
from flask import Flask, url_for, render_template, request
import spacy
from spacy import displacy

from stanza.utils.conll import CoNLL
nlp = spacy.load('en_core_web_sm')

HTML_WRAPPER = """<div style=" border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


app = Flask(__name__)
Markdown(app)


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index():
    # raw_text = "Bill Gates is An American Computer Scientist since 1986"
    # docx = nlp(raw_text)
    # html = displacy.render(docx,style="ent")
    # html = html.replace("\n\n","\n")
    # result = HTML_WRAPPER.format(html)

    return render_template('index.html')


@app.route('/extract', methods=["GET", "POST"])
def extract():
    if request.method == 'POST':
        raw_text = request.form['rawtext']
        docx = nlp(raw_text)
        print(str(docx))
        print(type(docx))
        html = displacy.render(docx, style="dep")
        html = Sanskrit.get_sans_html(filename='test.conll')
        html = html.replace("\n\n", "\n")
        result = HTML_WRAPPER.format(html)

    return render_template('result.html', rawtext=raw_text, result=result)


@app.route('/previewer')
def previewer():
    return render_template('previewer.html')


@app.route('/preview', methods=["GET", "POST"])
def preview():
    if request.method == 'POST':
        newtext = request.form['newtext']
        result = newtext

    return render_template('preview.html', newtext=newtext, result=result)


if __name__ == '__main__':
    app.run(debug=True)
