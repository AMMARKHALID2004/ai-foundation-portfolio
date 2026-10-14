import timer,time,caching,retry,rate_limit,logging_deco

api_call_count=0


@retry.retry(3)
def call_model_api(prompt):
    global api_call_count
    api_call_count+=1
    if api_call_count<2:
        raise ConnectionError("API call failed")
    return f"Response to : {prompt}"
        

@caching.memoize
def get_embedding(text):
    print("computing embedding...")
    time.sleep(1)  # pretend this is slow
    return [len(text), len(text) * 2]  # totally fake, just needs to return something

@timer.timer
@logging_deco.logger  # the stack of decorators applied runs from bottom to top. logger will run first and then timer will run
def preprocess_batch(data):
    return [x * 2 for x in data]  # pretend "preprocessing"


# Test 1: retry
print(call_model_api("hello"))

# Test 2: memoize — call twice with same text, confirm "computing embedding..." prints only once
print(get_embedding("some text"))
print(get_embedding("some text"))   # should NOT print "computing embedding..." again

# Test 3: stacked timer + logger, current order (@timer on top, @logger underneath)
print(preprocess_batch([1, 2, 3]))