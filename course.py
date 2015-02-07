import json

data = []
with open('documents/data.jason') as f:
    for line in f:
        data.append(json.loads(line))