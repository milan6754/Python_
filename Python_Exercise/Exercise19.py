
'''📝 Exercise 1
Create a function report(title, *messages, **extra)
Print title
Print all messages
Print all extra info
👉 Write the code and test it with 2–3 messages + 2 extra keyword arguments
'''
def report(title, *messages,**extra):
    print(f"title:{title}")
    for mess in messages:
        print(f"messsage:{mess}")

    for key, value in extra.items():
        print(f"{key}:{value}")

report(
    "Missing Items",
    "Hey, item not found",
    "Check inventory",
    "Notify supplier",
    age=12,
    address="SDK Street",
    phone_no=98499
)
'''📝 Exercise 2
Create a function order_summary(order_id, *items, **info)
Print order_id
Print all items
Print all info
👉 Write the code and test with 3 items + customer and total as keywords
'''
def order_summary(order_id,*items,**info):
    print(f"Id:{order_id}")

    for item in items:
        print(f"itmes:{item}")
    
    for key , value in info.items():
        print(f"{key}:{value}")
order_summary(
    101,
    "Apple",
    "Banana",
    "Orange",
    customer="Milan",
    total=25.50
)
'''📝 Exercise 3
Create a function event_log(event_type, *notes, **details)
Print event_type
Print notes one by one
Print details using key: value format
👉 Write the code and test it'''

def event_log(event_type,*notes,**details):
    print(f"Type:{event_type}")

    for note in notes:
        print(note)
    
    for key, value in details.items():
        print(f"{key}:{value}")

event_log(
    "Login Attempt",
    "User entered username",
    "Password accepted",
    timestamp="2025-12-31 16:00",
    ip_address="192.168.1.10"
)
'''🔥 Mini Challenge (optional)
Create a function flexible_calc(operation, *nums, **options)
If operation is "add" → sum all nums
If "multiply" → multiply all nums
If "round" in options → round the result to given decimal places'''
import math
def flexible_calc(operation, *nums,**options):
    if operation == "add":
        result= sum(nums)
    elif operation =="multiply":
        result= math.prod(nums)
    else:
        print("Invalid operations")
    if "option" in options:
        result = round(result,options["round"])
    
    return result



# Mini Challenge: flexible_calc
# Addition without rounding
print(flexible_calc("add", 2, 3, 5))


# Multiplication without rounding
print(flexible_calc("multiply", 2, 3, 4))


# Addition with rounding
print(flexible_calc("add", 2.456, 3.789, round=2))


# Multiplication with rounding
print(flexible_calc("multiply", 2.5, 3.2, round=1))
