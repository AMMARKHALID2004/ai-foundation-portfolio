counter=0

def retry(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                try:
                    print(f"{i+1 } call")
                    result=func(*args,**kwargs)
                    return result
                except Exception as e:
                    print(e)
                    last_exception=e
            raise last_exception  
            

        return wrapper
    return decorator

@retry(2)
def dummy():
    global counter
    counter+=1
    if counter<3:
        raise ValueError
    return "success"


if __name__=="__main__":
    dummy_func=dummy()
    print(dummy_func)