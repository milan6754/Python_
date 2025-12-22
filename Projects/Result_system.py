class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def is_pass_fail(self):
        if self.marks <40:
            return "Fail"
        return "Pass"
    
    def show_result(self):
        print(f"The student {self.name} is {self.is_pass_fail()}")
        


std1= Student("Milan",45)

print(std1.is_pass_fail())
std1.show_result()

std2=Student("Alex", 40)
std3=Student("John", 39)
std4=Student("Sara", 0)


std2.show_result()
std3.show_result()
std4.show_result()
