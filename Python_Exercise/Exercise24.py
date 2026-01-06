'''📝 Exercise 1
Create a class Person
__init__(name, age)
method introduce()
Output: "Hi, I am X and I am Y years old"'''
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old"

prsn1 = Person("milan",12)
print(prsn1.introduce())


'''📝 Exercise 2
Create a class Car
attributes: brand, speed
method accelerate() → increase speed by 10
method show_speed()'''

class Car:
    def __init__(self,brand,speed=0):
        self.brand = brand
        self.speed = speed
    
    def accelerate(self):
        self.speed +=10
        
    def show_speed(self):
        return f"Speed is:{self.speed}"

bmw = Car("porsche",23)

print(bmw.show_speed())

'''📝 Exercise 3
Create a class Student
attributes: name, marks
method is_passed()
Return "Passed" if marks ≥ 40 else "Failed"'''
class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    
    def is_passed(self):
        if self.marks >= 40:
            return f"{self.name} is Passed"
        else:
            return f"{self.name} is failed"

std1 = Student("Milan",42)
print(std1.is_passed())

'''🔥 Mini Challenge (Optional)
Convert one part of your To-Do app into a class:'''

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Added Task sucessful !")
    
    def show_task(self):
        for i , task in enumerate(self.tasks,1):
            print(f"{i}.{task}")
    def del_task(self,index):
        if 1<=index <=len(self.tasks):
            del self.tasks[index-1]
        else:
            print("Invaid number")
ok = TodoApp()
ok.add_task("wake up")
ok.add_task("Brush teeth")
ok.show_task()
ok.del_task(2)
print("-----------")
ok.show_task()

'''Create:
Animal class → name
Dog class → breed
Dog should inherit Animal
Add one method in Dog: sound() → prints "Bark"'''
class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name,breed):
     super().__init__(name)
     self.breed = breed

    def sound(self):
        print(f"{self.name} Bark")


tomy = Dog("tommy" ,"ok")
tomy.sound()

