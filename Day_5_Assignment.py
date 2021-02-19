"""
Make a generator to perform the same functionality of the iterator
"""
def infinite_sequence(): # to use for printing numbers infinitely 
    num = 0
    while True:
        yield num
        num += 1


  for i in infinite_sequence():
    print(i, end=" ")

"""
Try overwriting some default dunder methods and manipulate their default behavior
"""
     
class distance:
    def __init__(self, ft=0,inch=0):
        self.ft=ft
        self.inch=inch
    def __add__(self,x):
        temp=distance()
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)

d1=distance(3,10)
d2=distance(4,4)
print(f"d1= {d1} d2={d2}")

d3=d1+d2 # overridden the + operator __add__ 
print(d3)


"""
Write a decorator that times a function call using timeit
start a timer before func call
end the timer after func call
print the time diff

"""
import timeit

def time_function(inner_fun):
    
    def time(*args, **kwargs):
        t_start=timeit.default_timer()
        print(f"satrt time : {t_start}")
        inner_fun(*args, **kwargs)
        t_end=timeit.default_timer()
        print(f"end time : {t_end}")
        run_time=t_end-t_start
        print(f"execution time  : {run_time}")
    return time

@time_function
def my_loop_method(i):
    total=0
    print(f'I am a loop method to sum numbers in entered range having decorator to track time of execution!')
    for i in range(0,i):
        total +=i

my_loop_method(10000) # takes more execution time
my_loop_method(10)

