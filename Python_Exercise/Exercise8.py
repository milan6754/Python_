#List Comprehension: Generate a list of all palindromes in a given list of words.
things = ["milan","mom", "hello", "wow"]
allplindromes=[pal for pal in things if pal ==pal[::-1]]
print(allplindromes)

#Dictionary Comprehension: Create a dictionary where keys are numbers 1–10 
# and values are squared numbers.
squared_num = {x: x**2 for x in range(1,11)}
print(squared_num)

#Lambda + Filter: From a list of numbers, return only even numbers greater than 5.

nums = [1,2,3,4,5,6,7,8,9]

evens = list(filter(lambda x: x%2==0 and x>5,nums))
print(evens)

#Safe File Logger: Ask user for input and append it to a file safely, handle file errors.
try:
    user = input("Enter the any thing: ")
    with open ("Exercise7.txt","a") as file:
        file.write("\n"+user )

except (IOError, OSError) as file_error:
    print("File error:", file_error)
except (EOFError, KeyboardInterrupt):
    print("Input was interrupted.")
