"""
Improvise the guessing game from yesterday by providing 3 tries to the player
"""
import random


guess=random.randint(1,20)
num=int(input("Enter the number : "))
no_of_tries=0
while(no_of_tries<2):
    no_of_tries +=1
    if num == guess:
        print(f"Congratulations you did it in {no_of_tries} try")
        # Once guessed, loop will break
        break
    if num < guess:
        
        print("You entered a value lower than the real value")

        num=int(input(f"Enter the number : "))

    elif(num>guess):
      
        print("You entered a  value higher than the real value")

        num=int(input(f"Enter the number : "))

if(no_of_tries==2):
    print("You entered wrong value thress times, Better Luck Next time!")





"""
Given a list ['a', 'b', ...] print elements along with their position like 0: a, 1: b one per line
"""

char_list = ['a','b','c','d','e','f']

for position,char in enumerate(char_list):
    print(f"{position} :{char}")
    print("\n")


"""
Loop over a dict and print the value and key in the format value belongs to key.
"""

a_dict={'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

for Key,Value in a_dict.items():
    print(f"{Value} belongs to {Key}")
    print("\n")    




"""
write a function that accepts any number of args and prints them to the screen one per line
"""

def get_args(*args):# any number of args
    for name in args:
        print(f"\n {name}")

get_args("john", "jake", "jack","george", "jenny", "jason")    



"""
write a function that accepts any number of kwargs and prints the number of orgs
"""

def get_Kargs(**kwargs):# any number of key word args
    args_count=0
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        args_count +=1
    print(f" you have passed {args_count} arguments ")


get_Kargs(name= "test",language="py",creator="Jithin")

"""
Go through PEP 20 and let me know your fav one!
"""
#Readability counts.

"""
Do list comprehension to get odd numbers' squares from this list: [1, 3, 3, 4, 5, 6]
"""

num_list=[1, 3, 3, 4, 5, 6]

newlist = [x** 2 for x in num_list if x%2 != 0]

print(newlist)


"""
write a lambda expression to return average given a total and count
"""

total=int(input("Enter the total : "))
count=int(input("Enter the count : "))
avg = lambda total, count : total /count
print(f"Average of {total} having count {count} = {avg(total,count)}")





"""
Try list comp to get keys that are longer than 4 chars in a dict
implement nested list comp in any use case
"""

list_Kvalues={'name':'test','language':'py','creator':'Jithin','color':'green'}
print(list_Kvalues.keys())
key_grt_than_four = {k for k in list_Kvalues.keys() if len(k) >4 }

print(key_grt_than_four)
