import time

def rate_limit(seconds):
    def decorator(func):
        last_called=0
        def wrapper(*args,**kwargs):
            nonlocal last_called
            passed_time=time.time()-last_called
            if last_called==0 or passed_time>=seconds:
                last_called=time.time()
                result=func(*args,**kwargs)
                return result
            else:
                print("Not enough time has passed since the last function call")
        return wrapper
    return decorator


@rate_limit(2)
def hello():
    
    return "Hello World"


if __name__=="__main__":
    print(hello())
    print(hello())
    time.sleep(2.5)
    print(hello())
