'''📝 Exercise 1
Create a function:
Call it using keyword arguments.
👉 Write the function and one call.'''

def create_account(username, email, verified=False):
    return f"{username} | {email} | {verified}"

print(create_account(username="Milan",email="thapamilanmgr@gmail.com"))





'''📝 Exercise 2
Create a function:
Call it with:
urgent=True using keyword argument
👉 Write the code.'''
def send_message(to, message, urgent=False):
    return f"To:{to}|message:{message} |Urgent:{urgent}"

print(send_message(to="milan",message="Hello sir come to office",urgent=True))





'''📝 Exercise 3
Create a function:
Call it:
once using only positional arguments
once using keyword arguments (any order)
    ...
👉 Write both calls.'''

def book_ticket(city, price, vip=False):
    return f"City:{city} | price:{price} | VIP_status:{vip}"

print(book_ticket(city="Dubai",price=12,vip=True))


'''🔥 Mini Challenge (optional)
Create a function:
Call it without caring about order, using only keywords.'''


def register(name, age, country="Nepal", newsletter=True):
    return f"name:{name} | age: {age} | country:{country} |{newsletter}"
print(register(name="Milan",age=24,newsletter=False))
