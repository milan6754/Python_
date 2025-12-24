'''🧠 Exercise 1 — Basic Inheritance
Create:
Person class → name, age
Student class inherits PersonAdd method introduce() in both
👉 Call introduce() from a Student object'''

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def introduce(self):
        return f"hello my name is {self.name} and i am {self.age} year old"
class Student(Person):
    pass
    
std1 = Student("Milan",24)
print(std1.introduce())
    

'''🧠 Exercise 2 — Polymorphism
Create:
Shape class → area() (empty or default)
Rectangle, Circle inherit Shape
Override area()
👉 Call area() using a Shape reference'''
import math
class Shape:
    def area(self):
        return 0 
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length 
        self.width = width 
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return math.pi * self.radius **2

shapes = [Rectangle(2,2),Circle(4)]

for shape in shapes:
    print(shape.area())

'''🧠 Exercise 3 — Thinking (Answer in words)
Why is inheritance better than copying code?
because it helps to avoids dublication ,it is easy to maintain ,clear structure and scable

When can inheritance become harmful?
when the deep inheritance chains, inherit behaviour when not needed , 

Difference between method overriding and method overloading?
overriding is the child class and overloading is a same class ,
overriding parameter is same  but different in overloading 
overriding purpose is to change behaviour and overloading purpose is to handle multiple input types 

'''

