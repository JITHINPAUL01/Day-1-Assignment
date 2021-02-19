"""
Write an iterator yourself 
Create a class that implements __iter__ and __next__ methods.

It should accept a string and provide an iterator that traverses every other character
in the string i.e. given hello, provide h, l, o and StopIteration on consecutive next calls. Should work like below:
"""
import sys
class MyCustomClass:
    """Class to implement an iterator """
    

    def __init__(self,input_str):
        self.input_str = input_str
        self.start=0
        
    def __iter__(self):
        return self

    def __next__(self):  
        if self.start < len(self.input_str):
            output={self.input_str[self.start]}
            self.start =self.start +2
            return output
        else:
            raise StopIteration


# create an object
x = MyCustomClass('hello')

# create an iterable from the object
i = iter(x)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
#print(next(i))




"""
create a CSV file containing names and experience of the participants. Note: Not xls, just a comma separated plain text file.
"""
employee_details={'Jithin':'7 years','Bob':'10 years','Fred':'4 years','Mary':'2 years'}
try: 
    f = open("myfile_jithin_day3.txt", "w")
    for i in employee_details:
     f.write(f"{i} : {employee_details[i]} ,")
except:
    print("An exception occurred")


"""
write a program to traverse the current directory (recursively) and print only python file names.
"""
import os
#get directory for current folder
path = os.walk(".")

for root, directories, files in path:
    for file in files:
        if str(file[-3:]) == ".py":
         print(file)


print (f"Number of arguments:', {len(sys.argv)}, 'arguments.'")
print (f"Argument List:', {str(sys.argv)}")


"""
Rewrite the guessing game program to throw a custom error when the user is out of tries.
"""


import random

print("Welcome, To Guess The Number Game")

attempt = int(input("Choose the number of attempts between 1-10 in which you can guess the Number => "))

constant = random.randint(1, 100)

i = 1

while i <= attempt:

    try:

        random_num = int(input('Guess the Number : '))

        if random_num < constant and (random_num > constant-10):

            print("Your number Was close to, but Less than the generated Number ")

        elif random_num < constant:

            print("Your number Was less than the generated Number ")

        elif random_num > constant and (random_num < constant+10):

            print("Your number Was close to, but Greater than the generated Number ")

        elif random_num > constant:

            print("Your number Was Greater than the generated Number ")

        else:

            print("Yay !! You Guessed it right. The Number is ", constant)

            break

        i += 1

    except ValueError:

        print('error')

    if i > attempt:

        raise ValueError("Alas !! Your attempts are exhausted. The Number is ", constant)

"""
Rewrite the guessing game program to throw a custom error when the user is out of tries.
accept input from a user and handle type, value errors
"""
import random
attempt=0

try:
    attempt = int(input("Choose the number of attempts between 1-10 in which you can guess the Number => "))
except ValueError:
    print('entered value is no appropriate integer')
constant = random.randint(1, 100)

i = 1

while i <= attempt:

    try:

        random_num = int(input('Guess the Number : '))

        if random_num < constant and (random_num > constant-10):

            print("Your number Was close to, but Less than the generated Number ")

        elif random_num < constant:

            print("Your number Was less than the generated Number ")

        elif random_num > constant and (random_num < constant+10):

            print("Your number Was close to, but Greater than the generated Number ")

        elif random_num > constant:

            print("Your number Was Greater than the generated Number ")

        else:

            print("Yay !! You Guessed it right. The Number is ", constant)

            break

        i += 1

    except ValueError:

        print('Gussed value is not a number')

    if i > attempt:

        raise ValueError("OOPS..you are out of try. The Number is ", constant)
