#Sum of numbers 1 → n
#Ask user n and print sum from 1 to n.

n = int(input("Enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"The sum of 1 to n is: {sum}")


#Odd numbers in a range
#Ask user start & end, print all odd numbers.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start,end+1):
    if not i%2==0:
        print(i)

#Custom table function
#Ask user for number x and y, print table of x up to y.

x= int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

for i in range(1,y+1):
    print(f"{x}*{i}={x*i}")

#Even/Odd check for list
#Create a list of numbers, loop through, print which are even/odd

numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

