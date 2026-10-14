#The filter() function in Python is a elegant way to extract specific items
# from a list (or any iterable) based on a condition

fruits=['apple','orange','watermelon','mango','banana']

a=list(filter(lambda fruit:'e' in fruit,fruits))

print(a)

