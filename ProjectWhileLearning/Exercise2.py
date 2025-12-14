"""#first python code here we go 
print("hello world ")

#strings
str= "Milan T-h-a-pa"

strr="!!what!!"
string = ['Milan', 'is', 'learning', 'Python']
result = " ".join(string);
result2 = str.startswith("Milan")
result3 = str.endswith("Milan")
result4 = str.find("pa")
str1= str.upper(); #This method used to uppercase all char in the string 
str2= str.lower(); #this method used to lower all char in the string 
str3= strr.strip("!"); #this method used to remove and space and unique char in the string 
str4 = str.split("-");
messy = "milan  loves   python  loves programming  "
result= messy.strip().split();
final = " ".join(result)
print(final)

count= messy.count("loves");
ok = messy.title();

print(ok)
print(count)
print(messy.isupper())
print(messy.islower())
print(str1)
print(str2)
print(str3)
print(str4)
print(result);
print(result2);
print(result3)
print(result4)"""


class Car:
    wheel=4
    def __init__(self,make,model,year):
        self.make= make 
        self.model= model
        self.year = year
    
    def car_info(self):
        print(f"this is made by {self.make} | {self.model} |{self.year}")

car1 = Car("Elon","BMW" ,1997)
car2 = Car("Milan","Porshe" ,1973)

car1.car_info()
car2.car_info()
print(car1.wheel)
print(car2.wheel)