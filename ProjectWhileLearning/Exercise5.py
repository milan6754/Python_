
#Write a function:
#Returns sum from 1 → n

def sum_upto(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

print(sum_upto(4))


#Write a function:
#Returns True or False

def is_palindrome(word):
    reverse = word[::-1]
    if word ==reverse:
        return True
    else:
        return False
    
print(is_palindrome("mom"))


#Write a function:
#Takes a list
#Returns words longer than 3 characters in uppercase

def filter_long_words(words):
    for word in words:
        if len(word)>3:
            print(word.upper())
        
filter_long_words(["milan","mom","whatups","name"])



#Challenge 1
#Write a function that:
#Takes a list of numbers
#Returns only even numbers

def only_even(nums):
    even=[]
    for num in nums:
        if num%2==0:
            even.append(num)
    return even
print(only_even([1,2,3,4,5,6,7,8,9]))

#Challenge 2
#Write a function that:
#Takes a sentence
#Returns number of vowels
#Challenge 3 (Thinking)

def vowel(sentence):
    vowel_letter ="aeiouAEIOU"
    vowel_count=0
    for sen in sentence:
        if sen in vowel_letter:
            vowel_count+=1

    return vowel_count

print(vowel("milan"))


#Answer in words:

#Why is return more powerful than print?

#When should a function NOT print anything?

