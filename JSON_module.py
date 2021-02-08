import json
#Convert from JSON to Python
x = '{"name":"Priyansh","age":21,"city":"Auraiya"}'
y = json.loads(x)
print(y["age"])

#Convert from Python to JSON
a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
b = json.dumps(a)
print(b)

#other python objects conversion to json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Format the Result
z = {
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
print(json.dumps(z))
json.dumps(x, indent=4, separators=(". ", " = "))

#Order the Result
json.dumps(x, indent=4, sort_keys=True)