"""
Given a list of names, try printing unique names that are less than 5 character length and doesn't contain the character 'e'. 
names = ["john", "jake", "jack", "george", "jenny", "jason"]
"""

names = ["john", "jake", "jack", "george", "jenny", "jason"]
uni_Names = set(names)
for name in uni_Names:

  if len(name) < 5 and "e" not in name:

    print(name)



"""
Given a string python, try printing cython using slicing [start:stop] and concatenation. +
"""

print("\n")

name = "python"

print("c" + name[1:])


print("\n")
"""
Given a dictionary {"name": "python", "ext": "py", "creator": "guido"}, print both keys and values.
"""
dictionary = {"name": "python", "ext": "py", "creator":"guido"}

for key,value in dictionary.items():

  print(f"Key:{key},Value:{value}")

"""
Do FizzBuzz in Python
"""

print("\n")

for i in range(1,101):

  if i%3==0:

    print("Fizz")

  elif i%5==0:

    print("Buzz")

  elif i%3==0 and i%5==0:

    print("FizzBuzz")

  else:

    print(i)  




"""
Guessing Game. Accept a guess number and tell us if it's higher or less than the hardcoded number
"""
print("\n")

import random

guess=random.randint(1,20)

num=int(input("Enter the number : "))

while(guess!=num):

    if num < guess:

        print("you entered a  value lower than the real value")

        num=int(input("Enter the number : "))

    elif(num>guess):

        print("you entered a  value higher than the real value")

        num=int(input("Enter the number : "))

print("correct answer")
