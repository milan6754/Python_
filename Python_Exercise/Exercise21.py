'''📝 Exercise 1
Divide two numbers (a/b) safely
Catch ZeroDivisionError
Print "Cannot divide by zero" if error occurs'''

def div(a,b):
    try:
        div = a/b
        return div
    except ZeroDivisionError:
        return ("Cannot divided by zero")

print(div(4,0))

'''📝 Exercise 2
Convert input to integer
Catch ValueError
Print "Invalid number" if conversion fails'''

def convert():
    try:
        num = int(input("Enter the number: "))
        return (num)
    except ValueError:
        return("Invalid number")
print(convert())

'''📝 Exercise 3
Read a file "data.txt" safely
Catch FileNotFoundError
Print "File not found"'''

file_path = "/Users/milankumarthapa/Desktop/output.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Fine not found")

'''🔥 Mini Challenge (optional)
Create a function safe_divide(a, b)
Return a/b if possible
Return None if error occurs (any exception)
Always print "Attempted division" (use finally)'''

def safe_divide(a,b):
    try:
        print (a/b)
    except Exception as e:
        print(f"unexcepted error:{e}")
    finally:
        print("Attempted division")

safe_divide(4,0)