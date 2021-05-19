import json

data = {
        'Sudarshan Choudhary': ['311022'],
        '@manjeettanwar1026': ['302012', '302013'],
        '@zedd5321': ['302013', '302003', '302004', '302020', '302017', '302033', '302018']
        }

unique_code = set()

for user in data.keys():
    unique_code = unique_code.union(set(data[user]))
data['Sudarshan Choudhary'] = list(unique_code)

with open("data.json", "w") as myfile:
    json.dump(data, myfile)
