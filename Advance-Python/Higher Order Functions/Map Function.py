#Map is a higher order function which applies a defined
#operation on each value of an iterable
l=[1,2,3,4,5]

l2=list(map(lambda x:x+x,l))

for i in l2:
    print(i)