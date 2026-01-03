'''📝 Exercise 1
Create a function set_age(age)
If age < 0 → raise ValueError with "Age cannot be negative"
Else → return "Age set to X"'''

'''def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        return f"Age set to {age}"


try:
    print(set_age(-21))
except ValueError as e:
    print(f"error:{e}")'''


'''📝 Exercise 2
Create a custom exception InsufficientFundsError
Function withdraw(balance, amount)
If amount > balance → raise InsufficientFundsError("Not enough funds")
Else → return "Withdrawn X"'''

# Custom exception
class InsufficientFundError(Exception):
    pass

def withdraw(amount):
    balance = 1000
    if amount > balance:
        raise InsufficientFundError("Not enough funds")
    else:
        balance -= amount
        return f"Withdrawn {amount}"

try:
    print(withdraw(2000))
except InsufficientFundError as e:
    print("Error:", e)

'''📝 Exercise 3
Function login(user)
Allowed users: ["Milan", "Roshan"]
If user not in list → raise PermissionError("Access denied")
Else → return "Welcome USER"'''
def login(user):
    users=["Milan","Roshan"]
    if user not in users:
        raise PermissionError("Access denied")
    else:
        return f"Welcome {user}"
print(login("Milan"))


'''🔥 Mini Challenge (optional)
Create a function divide(a, b)
If b == 0 → raise ZeroDivisionError("Cannot divide by zero")
Else → return a/b'''

def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a/b
try:    
    print(divide(4,0))
except ZeroDivisionError as e:
    print("Error",e)