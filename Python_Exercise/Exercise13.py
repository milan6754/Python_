'''🧠 Exercise 1 — Encapsulation
Create a BankAccount class with:
private attribute __balance
methods:
deposit(amount)
withdraw(amount)
get_balance()

Rules:
Balance must never be negative
Deposit only positive amounts
👉 Try breaking the class from outside — you shouldn’t be able to.'''

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance 
        if self.__balance <0:
            raise ValueError("Balance must be positive")
    
    def deposit(self,amount):
        if amount<0:
            raise ValueError("Amount must be greater")
        
        self.__balance +=amount
        return self.__balance
    def withdraw(self,amount):
        if amount<0:
            raise ValueError("Amount must be greater")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -=amount
        return self.__balance
    def get_balance(self):
        return self.__balance
milan = BankAccount(1000)
print(milan.deposit(1000))
print(milan.withdraw(500))
print(milan.get_balance())

'''🧠 Exercise 2 — Getter & Setter
Create a Student class with:
private __marks
set_marks(marks) → validates (0–100 only)
get_marks()
grade() method (reuse your logic)'''
class Student:
    def __init__(self, marks=0):
        self.set_marks(marks)

    def set_marks(self, marks):
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        else:
            return "F"

milan = Student(85)
print(milan.get_marks())
print(milan.grade())
milan.set_marks(55)
print(milan.grade())



'''
🧠 Thinking (Answer in words)
Why is validation better inside a class than outside?

Because only the class can truly protect its own data.

What problem does encapsulation solve in real software?

Encapsulation solves system fragility.


Why is direct attribute access dangerous?
Direct attribute access is dangerous because it bypasses all the safeguards a class provides, allowing invalid 
or inconsistent data to enter the system.
'''

