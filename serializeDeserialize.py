import json
# print(json.dumps([1,'simple','list']))
x={'a':1,'b':2}
y= [1, "simple", "list"]
with open('jsontemp','w') as f:   ###serialising lists and dict
    # json.dump(x, f)
    json.dump(y,f)
# x = json.load(f)
with open('jsontemp') as f:       ####deserialising lists and dict
    xo= json.load(f)
print(type(xo))

import json
info_about_me={
    "Name":"Prathyusha",
    "Age":"29",
    "Children":"Yes"
}
python_dict={
    "x":1,
    "y":2
}
#####Python to JSON
json_object=json.dumps(python_dict)
print("Json Object: ",json_object)
#####Json to Python
python_d=json.loads(json_object)
print("Python Dictionary:",python_d)

#####Loading json to a file
with open("info.json",'w') as f:
    json.dump(info_about_me,f)
######Parsing from Json file to python
with open("info.json") as f1:
    info=json.load(f1)
print(info)

##############
print(json.dumps({"name": "John", "age": 30}))  ##dict ->	Object
print(json.dumps(["apple", "bananas"]))         ##list,tuple ->   Array
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))                      ##str ->String
print(json.dumps(42))                           ##int,float  -> Number
print(json.dumps(31.76))
print(json.dumps(True))                         ##True -> true
print(json.dumps(False))                        ##False -> false
print(json.dumps(None))                         ##None -> null
###############
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x,indent=4,separators=(". ", " = ")))   ##default ",:"