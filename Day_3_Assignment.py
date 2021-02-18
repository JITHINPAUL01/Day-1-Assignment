"""
dictionaries
given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict 
of squares { 1: 1, 2: 4, 3: 9}
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension
"""

list_nums=[1, 2, 3]
#print(list_nums)
created_dict =dict(zip(list_nums,[x** 2 for x in list_nums]))
print(created_dict)

new_list= list(created_dict.values())

print(new_list)

"""
set comprehension
given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. 
{1, 4, 9, 16, 25}
"""

list_nums=[1, 2, 5, 2, 3, 1, 4, 5]
square_list =[x** 2 for x in set(list_nums)]
print(square_list)


"""
Given a list of tuples with current and min balances:
 [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:
"""

new_dict=[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]


#dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}
Output = [item[:-1] for item in new_dict 
          if item[1] >= item[2]] 
print (Output)

#set of all balances {2000, -52, 900}

balance_list = [name for (_, name, _) in [item for item in new_dict]][:-1]

print (balance_list)

#list of account holders ["Guido", "Raymond", "Jack", "Brandon"]
account_holders=[name[0] for name in [item for item in new_dict]]

print (account_holders)

#dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}
rem_Balance_Dict = {name : min-balance for (name, balance, min) in new_dict if min > balance}     #3.d

print(rem_Balance_Dict)

#list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]
account_holders=[(name,balance) for (name,balance,_)  in new_dict if balance>0]
print (account_holders)



"""
Write a Developer class that has a code function and a languages list.
code function should accept a language param and if the language is in the languages list it should print code in <language>.
resume function that prints languages of the developer.
Write a SrDeveloper class that inherits Developer and adds review function. review should also be limited to languages list.
Write a TechLead class that inherits from SrDeveloper and adds design function
"""

class Developer:

    def __init__(self):
        self.languages=["C","C++","Java","Python","JS","JSON"]

   

    def code(self,lang):
        if lang not in self.languages:
            print("code not found")
        else:
            print(f"code in {lang}")
    
    
    def resume(self):
        print(self.languages)

input_language = (input("Enter a coding language: ")).strip()

print(input_language.__str__())

print(input_language.__repr__())
obj= Developer()
obj.code(input_language)
obj.resume()

class SrDeveloper(Developer):

    def __init_(self):
        self.reviews=[]
        super().__init__(self)

    def review(self,review):
        if(review in self.languages):
            self.reviews.append(review)
            print(self.reviews)

        

obj1 = SrDeveloper()

obj1.code("java")

obj1.review("dotnet")

class TechLead(SrDeveloper):



    def __init__(self):

        SrDeveloper.__init__(self)

    

    def design(self):                      

        print("Design called by TechLead")

obj3 = TechLead()

obj3.code("java")

obj3.code("C")

obj3.resume()

obj3.review("Java") 

obj3.review("Python") 

obj3.review("ruby") #Doesn't get appended as the Code is not in main listc

obj3.design()          #Object of Subclass calling all it's  functions





"""
import a func from a module and call it to print some output
import a func and rename it to use in your module from another
"""

from ImportModule import myfunction

myfunction()


from ImportModule import secondFunction as importedModule

importedModule()
