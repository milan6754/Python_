'''Exercise 1
Create a Student class with:
name
marks
method is_pass() → returns True/False'''

class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks=marks

    def is_pass(self):
        if self.marks > 30 :
            return True
        else:
            return False
milan = Student("Milan",34)
print(milan.is_pass())

'''Exercise 2
Create a BankAccount class:
balance
deposit()
withdraw()
prevent negative balance'''

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

        print(f"The amount is :{self.balance}")



    def deposit(self,amount):
        
            if amount<0:
                raise ValueError("Negative Value")
            
            self.balance +=amount
            return f"The amount {amount} is deposited | Total balance is {self.balance}"
        
    def withdraw(self,amount):
        if amount<0:
            raise ValueError("Negative value")
        elif self.balance>amount:
                print("Insufficent balance ")
        else:
            self.balance -=amount
            return f"The amount {amount} is deduct | Remaining balance is {self.balance}"

milan = BankAccount(1000)
print(milan.deposit(2000))
print(milan.withdraw(100))



'''Exercise 3 (Thinking)
Answer in words:
Why is OOP better than only functions?
because OOP contain enpasulation , inhertance , polymorphisim , abstraction which makes  it better than function 
What is the role of self?
the role of self is to indicate this data is belong to this method 
'''

