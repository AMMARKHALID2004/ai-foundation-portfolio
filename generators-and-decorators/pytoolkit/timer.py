import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        
        finish_time=time.time()-start
        print("the finish time for the function ", func.__name__," is ",finish_time)
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"


if __name__=="__main__":
    result = slow_function()
    print(result)  # should print "done"