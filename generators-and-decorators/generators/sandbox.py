#Problem number 1

import sys
def square(n):

    list_1=[x**2 for x in range(n)]

    return list_1

# list loads all elements in memory at once, it will consume too much memory

demo_gen=square(10000000)
print(sys.getsizeof(demo_gen))

def gen(n):
    for i in range(n):
        yield i**2

#generator loads each element in memory one by one , so it will take less memory
gen1 = gen(10000000) 
print(sys.getsizeof(gen1))

#Problem number 2

def gen_demo():
    yield 1
    yield 2
    yield 3

demo=gen_demo()


print(next(demo))
print(next(demo))
print(next(demo))
# generator does not act like return statement, it will continue next time where it left 
try:
    print(next(demo))
except StopIteration:
    print("exhausted")

# for loop will not throw stopiteration exception because for loop handles iterators's stop exceptions
# under the hood like range,generators,lists etc
for i in demo:
    print(i)


