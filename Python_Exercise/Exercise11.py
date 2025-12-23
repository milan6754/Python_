'''🔹 Exercise 1
Create a Student class with:
name
marks
grade() method
≥ 80 → A
≥ 60 → B
≥ 40 → C
else → Fail'''

class Student:
    def __init__(self,name, marks):
        self.name = name 
        self.__marks = marks
    def grade(self):
        if self.__marks >=80:
            return "Congrats Grade 'A'"
        elif self.__marks>=60:
            return "Congrats Grade 'B'"
        elif self.__marks>=40:
            return "Congrats Grade 'C'"
        else:
            return "Fail"

std1 = Student("Milan",90)

print(std1.grade())




'''🔹 Exercise 2
Create a Rectangle class:
length
width
area()
perimeter()'''

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)

area1 = Rectangle(2,2)
print(area1.area())
print(area1.perimeter())


