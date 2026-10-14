counter = 0

def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        global counter

        key = (args, tuple(sorted(kwargs.items()))) # order matters in the tuples so f(a=1, b=2) and f(b=2, a=1) are not same.That is why we are sorting

        if key in cache:
            return cache[key]

        counter += 1      # New value being computed
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@memoize
def fib(n):
    print(n)
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__=="__main__":
    print(fib(100))
    print("New computations:", counter)