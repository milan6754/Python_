'''📝 Exercise 1
Create a function square(number)
It should return the square.
👉 Write the code.'''
def square(number):
    sqr = number **2
    return sqr
print(square(2))

'''📝 Exercise 2
Create a function full_name(first, last)
It should return: "First Last"

👉 Write the code.'''
def full_name(first,last):
    return f"{first} {last}"

print(full_name("milan","thapa"))

'''📝 Exercise 3

Create a function is_even(num)
Return True if even, else False

👉 Write the code.'''

def is_even(num):
    return True if num%2==0 else False
print(is_even(3))


'''🔥 Mini Challenge (optional)
Create a function calculator(a, b, operation)
If operation is "add" → return sum
If "sub" → return difference
Example:'''

def calculator(a,b,operation):
    if operation=="add":
        return a+b
    elif operation=="sub":
        return a-b
    elif operation == "div":
        return a/b
    elif operation =="mul":
        return a*b
    else:
        return "invalid operation"
    
print(calculator(4,2,"sub"))