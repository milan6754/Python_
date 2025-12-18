name = input("Enter the name:")
age = int(input("Enter your age:"))
print(f"hello {name}, you will be {age+1} next year")



a = int(input("Enter the first number: "))
b = int(input("Enter the secone number: "))
print(f"Sum of num: {a+b}")
print(f"Mulof num: {a*b}")
print(f"Div of num: {a/b}")



for i in range(1,21):
    print(i)



for num in range( 1,21):
    if num%2==0:
        print(num)


    
num = int(input("Enter the number:"))

for i in range(1,11):
    print(f"{num} * {i} = {num * i }")



def even_or_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

even_or_odd(21)


def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")


table(20)

#im just building somthing on my own 

