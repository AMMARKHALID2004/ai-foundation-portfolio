# zip() = Combines multiple iterables (lists, tuples, sets, dict)
#             into a single iterator of tuples.
#             Makes managing multiple indices easier.

list1=[1,2,3,4,5,6,7]
list2=[8,9,10,11,12,13,14,15]

list3=list(zip(list1,list2))

print(list3)

for i,j in list3:
    print(i,j)


# Iterable Unpacking

#* is used for avoiding unpacking error if there exists more items than we expect

t=[(1,2),(3,45,13),(34,13,141,14)]
for i,j,*extras in t:
    print(i,j)

# *_ is used for ignoring extra values (Convention)
for i,j,*_ in t:
    print(i,j)