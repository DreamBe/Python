import json

data = {
    'no': 1,
    'name': 'Shark',
    'url': 'www.panda.tv'
}

json_str = json.dumps(data)

print("----", data)
print("Orignal:", repr(data))
print("JSON:", json_str)

data2 = json.loads(json_str)
print("data2['name']:", data2['name'])
