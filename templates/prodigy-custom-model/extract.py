from prodigy.components.db import connect

db = connect()
all_dataset_names = db.datasets
examples = db.get_dataset("data")
# print(all_dataset_names)
print(examples)
# for i in range(len(examples[0]["relations"])):
#     print(examples[0]["relations"][i]["head"])
#     print(examples[0]["relations"][i]["label"])
#     print(examples[0]["relations"][i]["child"])
print(examples[0]["text"])
conll_str = examples[0]["text"].split(" ")
for i in range(len(examples[0]["relations"])):
    if examples[0]["relations"][i]["label"].lower()!='root':
        conll_str[i] = str(i+1) + "\t" + conll_str[i] + "\t" + str(examples[0]["relations"][i]["head"]+1) + "\t" + examples[0]["relations"][i]["label"]
    else:
        conll_str[i] = str(i+1) + "\t" + conll_str[i] + "\t" + str(0) + "\t" + examples[0]["relations"][i]["label"]
    if i!=len(examples[0]["relations"])-1:
        conll_str[i] += '\n'
final_str = ""
for i in range(len(conll_str)):
    final_str = final_str+conll_str[i]
print(final_str)
f = open("file.conll", "w")
f.write(final_str)
f.close()