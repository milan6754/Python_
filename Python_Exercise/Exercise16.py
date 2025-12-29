'''📝 Exercise 1
Create a function power(base, exponent=2)
Return base raised to exponent
Default exponent should be 2
👉 Write the code.'''

def power(base,exponent=2):
    return base ** exponent
print(power(2))

'''📝 Exercise 2
Create a function introduce(name, country="Nepal")
Return: "My name is X from Y"
👉 Write the code.'''
def introduce(name, country = "Nepal"):
    return f"My name is {name} from {country}"

print(introduce("Milan"))

'''📝 Exercise 3
Create a function order_item(item, quantity=1)
Return: "Ordered <quantity> <item>"
👉 Write the code.'''
def order_item(item,quantity=1):
    return f"Ordered:{quantity} {item}"

'''🔥 Mini Challenge (optional)
Create a function login(username, is_admin=False)
If is_admin is True → return "Welcome Admin"
Else → return "Welcome User"'''

def login(username, is_admin = False):
    if is_admin:
        return "Welcome Admin"
    else:
        return "Welcome User"

print(login("Milan"))
