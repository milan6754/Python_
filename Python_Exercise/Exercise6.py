"""Exercise 1
Create a dictionary for a book:
title
author
year
Print all key-value pairs."""

books = {
    "title":"The rich dad and poor dad",
    "author":"Robort",
    "year":1990
}
for  key , value in books.items():
    print(key,value)

"""Exercise 2
Ask user for 5 words.
Store them in a list.
Convert list to set.
Print unique words."""
a=0
word_list = []
while a<5:
    words = input("Enter the five words")
    word_list.append(words)
    a+=1

word_set = set(word_list)
print(word_set)


"""Exercise 3 (Thinking)
Answer in words:
Why is dictionary faster than list for lookup?
because it uses hasing , the loopup  is 0(1),
while list uses 0(n) for most of the search cases 

When should you NOT use a set?
dont use set when you need dublicate value
dont use set when you need order
dont use when you need index based value 

"""





