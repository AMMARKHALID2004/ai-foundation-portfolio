from functools import lru_cache

#Using recursion to multiply two numbers
def multiply(a,b):
    if b==1:
        return a
    else:
        return a+ multiply(a,b-1)
    
print(multiply(10,67))


#factorial using recursion

def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))


#checking palindrome using recursion

def palindrome(string):
    if len(string)<=1:
        return "palindrome"

    else:
        if string[0]==string[-1]:
            return palindrome(string[1:-1])
        else:
            return "not a palindrome"

print(palindrome('MADAM'))


#fibonnaci series using recursion without caching (it will take too much time )


# def fibonnaci(num):
#     if num<=1:
#         return num
#     else:
#         return fibonnaci(num-1) + fibonnaci(num-2)
    
# print(fibonnaci(40))


#fibonnaci series using recursion with caching

@lru_cache (maxsize=None)
def fibonnaci(num):
    if num<=1:
        return num
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)
    
print(fibonnaci(500))
print(fibonnaci.cache_info())