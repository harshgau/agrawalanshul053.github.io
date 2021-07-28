import uuid
from spacy.displacy.templates import (
    TPL_DEP_SVG,
    TPL_DEP_WORDS,
    TPL_DEP_WORDS_LEMMA,
    TPL_DEP_ARCS,
    TPL_ENTS,
)
from spacy.tokens import Doc, Span
from spacy.errors import Errors, Warnings
from spacy.displacy.templates import TPL_ENT, TPL_ENT_RTL, TPL_FIGURE, TPL_TITLE, TPL_PAGE
from spacy.util import minify_html, escape_html, registry
from spacy.errors import Errors
import warnings


DEFAULT_LANG = "en"
DEFAULT_DIR = "ltr"
_html = {}
RENDER_WRAPPER = None



def get_sans_html(filename=None):
    offset_x = 50                                                                          # x-coordinate of starting point of first word in svg box
    distance = 175                                                                         # distance_between_words
    data_string_list = list(open(filename))                                                
    arrow_stroke = 2                                                                       # stroke-width of arc
    arrow_spacing = 20
    word_spacing = 45
    compact = False
    arrow_width =  6 if compact else 10
    sentence_length = len(data_string_list)                                                # number of words in the string
    data = [(data_string_list[i].strip()).split('\t') for i in range(sentence_length)]
    # print(data)
    words = [data[i][1] for i in range(sentence_length)]
    tags = [data[i][2] for i in range(sentence_length)]
    dep = [data[i][5] for i in range(sentence_length)]
    x = [50+i*175 for i in range(sentence_length)]                                         # x-coordinate of starting point of all words in svg box
    width = offset_x + sentence_length * distance                                          # width of svg box
    id  = uuid.uuid4().hex                                                                 # id for <svg> tag
    color = "#000000"                                                                      # color in <svg> tag
    bg = "#ffffff"                                                                         # background color for <svg> tag
    dir = "ltr"                                                                            # direction inside <svg> tag
    lang = "en"                                                                            # language inside svg tag
    font = "Arial"                                                                         # font inside <svg> tag
    heads = [((int(data[i][4])-1) if int(data[i][4])>0 else 0) for i in range(sentence_length)]                              # heads of words
    # print(heads)
    arcs = []
    for i in range(sentence_length):
        if i < heads[i]:
            arcs.append(
                {
                    "start": i,
                    "end": heads[i],
                    "label": dep[i],
                    "dir": "left"
                }
            )
        elif i > heads[i]:
            arcs.append(
                {
                    "start": heads[i],
                    "end": i,
                    "label": dep[i],
                    "dir": "right",
                }
            )
    parsed = {"arcs" : arcs}
    # print(parsed)
    levels = [arc["end"]-arc["start"] for arc in parsed["arcs"]]
    highest_level = max(levels)
    # print(highest_level)
    offset_y = distance / 2 * highest_level + arrow_stroke
    height = offset_y + 3 * word_spacing
    y = offset_y + word_spacing


    # Creating code for words
    rendered_words = []
    for i in range(sentence_length):
        s = TPL_DEP_WORDS.format(text=words[i], tag=tags[i], x=x[i], y=y)
        rendered_words.append(s)




    # Creating code for arc
    rendered_arcs = []
    for i in range(sentence_length):
        start = parsed["arcs"][i]["start"]
        end = parsed["arcs"][i]["end"]
        label = parsed["arcs"][i]["label"]
        dir = parsed["arcs"][i]["dir"]
        if end-start == 1:
            compact = True
        else:
            compact = False

        if start < 0 or end < 0:
            error_args = dict(start=start, end=end, label=label, dir=dir)
            raise ValueError(Errors.E157.format(**error_args))
        level = levels[i]
        x_start = offset_x + start * distance + arrow_spacing
        if dir == "rtl":
            x_start = width - x_start
        y = offset_y
        x_end = (
            offset_x
            + (end - start) * distance
            + start * distance
            - arrow_spacing * (highest_level - level) / 4
        )
        dif = x_end-x_start
        if dir == "rtl":
            x_end = width - x_end
        y_curve = offset_y - level * distance / 2
        if compact:
            y_curve = offset_y - level * distance / 6
        if y_curve == 0 and max(levels) > 5:
            y_curve = -distance
        arrowhead = get_arrowhead(dir, x_start, y, x_end, arrow_width)
        if label == 'root':
            continue
        arc = get_arc(x_start, y, y_curve, x_end, compact)
        label_side = "right" if dir == "rtl" else "left"
        rendered_arc =  TPL_DEP_ARCS.format(
            id=id,
            i=i,
            stroke=arrow_stroke,
            head=arrowhead,
            label=label,
            label_side=label_side,
            arc=arc,
        )
        rendered_arcs.append(rendered_arc)
        # print(rendered_arc)
    # print(rendered_words)
    # print('#######################################################################################################################################################')
    # print(rendered_arcs)
    content = "".join(rendered_words)+"".join(rendered_arcs)
    content = content.replace("\n\n",'\n')
    content = content.strip()
    return TPL_DEP_SVG.format(
            id=id,
            width=width,
            height=height,
            color=color,
            bg=bg,
            font=font,
            content=content,
            dir=dir,
            lang=lang,
            )




def get_arc( x_start, y, y_curve, x_end, compact):
    """Render individual arc.

    x_start (int): X-coordinate of arrow start point.
    y (int): Y-coordinate of arrow start and end point.
    y_curve (int): Y-corrdinate of Cubic Bézier y_curve point.
    x_end (int): X-coordinate of arrow end point.
    RETURNS (unicode): Definition of the arc path ('d' attribute).
    """
    template = "M{x},{y} C{x},{c} {e},{c} {e},{y}"
    if compact:
        template = "M{x},{y} {x},{c} {e},{c} {e},{y}"
    return template.format(x=x_start, y=y, c=y_curve, e=x_end)

def get_arrowhead(direction, x, y, end, arrow_width):
    """Render individual arrow head.

    direction (unicode): Arrow direction, 'left' or 'right'.
    x (int): X-coordinate of arrow start point.
    y (int): Y-coordinate of arrow start and end point.
    end (int): X-coordinate of arrow end point.
    RETURNS (unicode): Definition of the arrow head path ('d' attribute).
    """
    # arrow_width = 10
    if direction == "left":
        pos1, pos2, pos3 = (x, x - arrow_width + 2, x + arrow_width - 2)
    else:
        pos1, pos2, pos3 = (
            end,
            end + arrow_width - 2,
            end - arrow_width + 2,
        )
    arrowhead = (
        pos1,
        y + 2,
        pos2,
        y - arrow_width,
        pos3,
        y - arrow_width,
    )
    return "M{},{} L{},{} {},{}".format(*arrowhead)

# filename = 'test.conll'
# get_sans_html(filename = filename)