#reduce() is the "finisher." It takes a collection of values and rolls
# them up  into a single cumulative result (like a sum, a product, or a concatenated string).

# The reduce(function, iterable) function applies a rolling computation to sequential pairs of values.

# 1. It takes the first two elements and applies the function.

# 2. It takes that result and the next element, applying the function again.

# 3. It continues until only one value remains.

import functools

l=['apple','mango','pineapple','banana','apple','watermelon']

l2=[1,2,3,4,5,6,7,8,9,10]

a=functools.reduce(lambda x,y: x is y,l)

b=functools.reduce(lambda x,y:x+y,l2)

print(a)

print(b)


