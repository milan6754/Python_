'''📝 Exercise 1
Create a function add_all(*numbers)
Return the sum of all numbers
👉 Write the code.'''

def add_all(*numbers):
    return sum(numbers)

print(add_all(1,2,3,4,5))

'''📝 Exercise 2
Create a function max_value(*values)
Return the largest number
👉 Write the code.'''

def max_value(*values):
    return max(values)

print(max_value(1,2,3,4,5,6,7,8,9))

'''📝 Exercise 3
Create a function print_names(*names)
Print each name on a new line
👉 Write the code.'''

def print_names(*names):
    for name in names:
        print(name)
 
print_names("Milan","Roshan","Manisha")

'''🔥 Mini Challenge (optional)
Create a function average(*numbers)
Return the average
If no numbers are passed, return 0'''
def average(*numbers):
    if not numbers:
        return 0 
    
    return sum(numbers)/len(numbers)

print(average())

'''📝 Exercise 1
Create a function user_info(**details)
Print each key and value on a new line
👉 Write the code.'''

def user_info(**details):
    for key , value in details.items():
        print(f"{key}:{value}")

user_info(name="Milan",age=21,address="duabi")

'''📝 Exercise 2
Create a function product(**data)
If "price" exists → print price
Else → print "Price not available"
👉 Write the code.'''
def product(**data):
    return data["price"] if "price" in data else "Prince not available"

print(product(name="Cube",price=12,qunty=12))

'''📝 Exercise 3
Create a function settings(**options)
If "debug" is True → print "Debug mode ON"
Otherwise → print "Debug mode OFF"
👉 Write the code.'''

def settings(**options):
    if options.get("debug"):
        return "Debug mode ON"
    return "Debug mode OFF"

print(settings(debug=False))
'''🔥 Mini Challenge (optional)
Create a function register_user(name, **extra)
Print name
Print all extra info
Example:
register_user("Milan", age=24, country="Nepal", premium=True)'''

def register_user(name,**extra):
    print(f"{name}")
    for key , value in extra.items():
        print(f"{key}:{value}")

register_user("Milan",age=24,country = "Nepal", premium=True)
