#Lambda Function :

#1. It has no name
#2. It returns nothing
#3. It is used with higher order functions
#4. It is not used for code reusability

#Syntax--> lambda input:expression

var = lambda x: x ** 2
print(var(9))

#Higher order function uses other functions within itself

l=[12,45,13,151,52,52,13,1415,1,91,11]

def return_sum(func,l):
    result=0
    for i in l:
        if func(i):
            result=result+i
    return result

x = lambda even: even % 2 == 0
y= lambda odd: odd%2!=0
z= lambda multiple_of_three: multiple_of_three%3==0

print(return_sum(z,l))
