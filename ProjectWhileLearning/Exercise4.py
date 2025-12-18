#Exercise 1
#Ask user for 5 numbers, store in list, print:
#sum
#average
#max
#Min
'''
x=0
nums = []
while x <5:
    num = int(input(f"Enter the {x+1} number:"))
    nums.append(num)
    x+=1
print(nums)

sum = 0 
for num in nums:
    sum+=num

print(f"The sum of List are {sum}")

average = sum/len(nums)

print(f"The average is {average}")

min = min(nums)
max = max(nums)

print(f"The min value is {min}")
print(f"The max value is {max}")

=================================
#Exercise 2
#Ask user for a word and:
#reverse it
#check if palindrome

word = input("Enter a word: ").lower()

reverse = word[::-1]
print(reverse)

if word ==reverse:
    print("This is palindrome")

else:
    print("This is not palindrome")

Exercise 3

Given a list of names:

convert all to uppercase

print names longer than 4 characters


#Exercise 3
#Given a list of names:
#convert all to uppercase
#print names longer than 4 characters

names = ["milan","thapa","appl","ball"]

for name in names:
    upper = name.upper()
    if len(upper)>4:
        print(upper)



🔥 Day 3 Mini Challenge (Optional but Powerful)

Ask the user to enter 5 words, store in a list.

Print all words reversed.

Print only palindromes.

Print words longer than 3 characters in uppercase.

This combines everything you learned today.'''
x=1
list=[]
while x <6:
    words= input(f"Enter the  word: ")
    list.append(words)
    x+=1

for name in list:
    rev = name[::-1]
    print(rev)

    if name==rev:
        print(f"this is palindromes {name}")
    
    if len(name)>3:
        print(name.upper())




