import prodigy
from prodigy.components.loaders import JSONL
from prodigy.components.preprocess import add_tokens
import spacy

@prodigy.recipe("custom-dep")
def custom_dep_recipe(dataset, source):
    stream = {"text": "Yasyam gfhezu atislakzrataya alekyaM vidAtum asaknuvantaH yuvAnaH pratibimbitaaNgAH ratnaBittIH sajIvacitrAH iva cakruH."}                          # load the data
    stream = add_relations_to_stream(stream)        # add custom relations
    stream = add_tokens(spacy.blank("en"), stream)  # add "tokens" to stream
    dic = list(open('prodigy.jsonl'))
    # print(dic)
    html = "".join(dic)
    # print(html)

    return {
        "dataset": dataset,      # dataset to save annotations to
        "stream": stream,        # the incoming stream of examples
        "view_id": "blocks",  # annotation interface to use
        "config": {
            "blocks": [
                {"view_id": "relations"},
                {"view_id": "html", "html_template": """<form method="get" action="F:\Downloads\Website-final\templates\prodigy-custom-model\file.conll"><button type="submit">Download</button></form>"""},
                # {"view_id": "html", "html_template": """<a href="" download><button>Download</button></a>"""},
            ],
            "labels": ["root", "axikaranam", "karanam", "karma", "prayojanam", "viseranam", "karwa", "prawiyogi", "anuyogi"]  # labels to annotate
        }
    }
def add_relations_to_stream(stream):
#    custom_model = load_your_custom_model()
#   
#   deps, heads = custom_model(eg["text"])
    deps = ["axikaranam", "axikaranam", "karanam", "karma", "prayojanam", "viseranam", "viseranam", "karwa", "karma", "prawiyogi", "anuyogi", "root"]
    heads = [11, 4, 4, 4, 11, 7, 7, 11, 11, 10, 8, 11]
    stream["relations"] = []
    for i, (label, head) in enumerate(zip(deps, heads)):
        stream["relations"].append({"child": i, "head": head, "label": label})
    yield stream


# dic = custom_dep_recipe("data", "source")