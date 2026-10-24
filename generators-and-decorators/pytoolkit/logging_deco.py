import functools

def logger(func):
    @functools.wraps(func)# it will just point the add to the wrapper.The functools.wraps() gets the metadata of the func which is actually the add function
                           # if we don't write @functools.wraps() it will output wrapper instead of add 
    def wrapper(*args,**kwargs):
        print(func.__name__)
        print("args:",args,"kwargs:",kwargs)
        result=func(*args,**kwargs)
        print(result)
        return result
    return wrapper
        
@logger
def add(a,b):
    return a+b
if __name__=="__main__":
    my_function=add(a=9,b=10)
    print(my_function)