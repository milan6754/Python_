'''Exercise 1 — File Write
Ask user for their name and age
Save to a file called user.txt'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
with open("Exercise7.txt","w") as file:
    file.write(f"Name:{name}\nAge:{age}")
    file.close()
print("The file is created....")

'''Exercise 2 — File Read

Read user.txt and print its content'''

with open("Exercise7.txt","r") as file:
    print(file.read())


'''Exercise 3 — Safe Calculator
Ask user for two numbers
Print division
Handle:
non-number input
division by zero'''

try:
    num1= int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print(f"The division of numbers : {num1/num2}")

except ZeroDivisionError:
    print('cannot divisable by zero')

except ValueError:
    print("input must be number")


'''Exercise 4 — Append Mode
Every time program runs:
Ask user for a note
Append it to notes.txt'''

note = input("Enter the note")

with open("Exercise7.txt","a") as file:
    file.writelines(note)
    file.close()

