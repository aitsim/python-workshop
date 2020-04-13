
# hada db dict 
test = {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
# In Python, JSON objects can be directly loaded as Python dictionaries 
# using the “json.load()” method from the json module. After loading the 
# JSON as a dictionary, the operations on the object are identical to 
# that of a normal dictionary object.
#  JSON is a specification for serializing 
# certain data structures into a byte stream.
for j in test["menuitem"]:
  print(j)

#  load json files or json data s

print("--------------------------")

test = '''{
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
  '''

import json 

content = json.loads(test)


for j in content["menuitem"]:
      del j["onclick"]


print(content)
content=json.dumps(content,indent=1)

print(content)

# deserialize a str ,bytes array content containing a json document to python object
# json.loads()

# serialize object to a json formated string 
# json.dumps()

mydict={}
mydict["name"]=123
print(mydict)


myseconddict=dict()
mydict["name"]=123
print(mydict)




