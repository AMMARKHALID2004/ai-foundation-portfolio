# problem 1 
def func(): 
    a=10

print(a) #NameError: name 'a' is not defined

#problem 2 

b=90

def modify(): #fails
    b+=1

print(modify())

def modify1():
    global b
    b+=1
print(modify1())

#problem 3

def outer():
    c=9
    def inner(): #fails
        c+=2
    return inner

print(outer()())

def out():
    d=9
    def inn():
        nonlocal d
        d+=2
    return inn

print(out()())