class Person:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        return "I am a peron"
    
class Student(Person):
    def __init__(self, name ,marks):
        super().__init__(name)
        self.marks=marks

    def is_pass(self):
        return self.marks>30
    
s1 = Student("Milan",30)
print(s1.name)
print(s1.marks)
print(s1.is_pass())


'''🔹 Exercise 1
Create:
Animal class → sound()
Dog, Cat inherit it
Override sound()'''

class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "meow"
dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())

'''🔹 Exercise 2
Create:
Employee → name, salary
Manager inherits Employee
Add bonus() method'''

class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary=salary
class Manager(Employee):
    def bonus(self):
        return self.salary * 0.5 + self.salary
mgr = Manager("Milan",2000)
print(mgr.bonus())


'''🔹 Exercise 3 (Thinking)
Answer in words:
Difference between inheritance vs composition?

Why is polymorphism powerful?
When should you NOT use inheritance?'''