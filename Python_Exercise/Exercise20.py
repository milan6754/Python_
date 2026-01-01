'''📝 Exercise 1
Create a decorator simple_logger
Print "Function started"
Call the function
Print "Function ended"
Apply it to a function task() that prints "Doing task".
👉 Write the code.'''

def simple_logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper
    

def task():
    print("doing task")

decorated = simple_logger(task)
decorated()
'''📝 Exercise 2
Create a decorator auth_check
Print "Checking access"
Call the function
Apply it to a function view_profile(name)
Call it with a name.
👉 Write the code.'''
def auth_check(func):
    def wrapper(*args,**kwargs):
        print("Checking access")
        return func(*args,**kwargs)

    return wrapper

@auth_check
def view_profile(name):
    print(f"Viewing profile of {name}")

view_profile("Milan")


'''📝 Exercise 3
Create a decorator timer_like
Print "Start"
Call the function
Print "End"
Apply it to a function process(data).
👉 Write the code.'''
def timer_like(func):
    def wrapper(*args,**kwargs):
        print("Start")
        result = func(*args,**kwargs)
        print("End")
        return result
    return wrapper

@timer_like
def process(data):
    print(f"processing:{data}...")
process("User Data")


'''🔥 Mini Challenge (optional)
Create a decorator uppercase_output
It should capture the function’s return value
Convert it to uppercase
Return it

Example:'''
def uppercase_output(func):
    def wrapper():
        return func().upper()
    
    return wrapper

@uppercase_output
def greet():
    return "hello"

print(greet()) 