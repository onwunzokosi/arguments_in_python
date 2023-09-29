"""
i=10
while i>=1:
    print(i)     #reverse on a loop
    i-=1

def greet():
    print("hello, jenny")       #an example of a function
greet('meith')

def num(a,b):
    print(a+b)
num(6,7)            #an example of positional argument

def intro(name,dept):
    print(f"hi, i'm {name} and i'm from {dept} department")
intro(dept="bch",name="frank")            #an example of keyword argument

def intro(name,dept,subject="CHEM"):        #an example of default argument
    print(f"hi, i'm {name} and i'm from {dept} department and my favourite course is {subject}")
intro("frank","bch","clinical")

def num(*alphabet):
    d=0
    for i in alphabet:
        d+=i    #if the print statement is written under the loop, it shows each step of the calculation
    print(d)    #but this gives the total calculation    
num(7,8,10,15,100,20,17,70)
"""
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info_person(name="frank",age=30,dept="CSS")