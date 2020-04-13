import json


with open("states.json" ,"r") as js:
    data=json.load(js)
    data = json.dumps(data,indent=2)
    # for con in data["states"]:
    #         print(con)

    for state in data['states']:
      del state['abbreviation']

    # write a an object
    with open('new_states.json', 'w') as f:
        json.dump(data, f, indent=2)


