import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
print(y)

# the result is a Python dictionary:
print(y["city"])
print(y["name"])
print(y["age"])


# string = "Hello 12345 World"
# numbers = [x for x in string if x.isdigit()]
# letters=[y for y in string if y.isalpha()]
# print (numbers)
# print (letters)