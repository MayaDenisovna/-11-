import time

def profile_func(func):
    
    def wrapper(*args,**kwargs):
        
        start_time=time.perf_counter()
        
        result=func(*args,**kwargs)
        
        end_time=time.perf_counter()
        
        execution_time=end_time-start_time
        
        print({'execution_time_sec':execution_time})
        
        return result
    
    return wrapper

@profile_func
def fib(n):
    
    if n<=1:
        return n
    
    return fib(n-1)+fib(n-2)

print(fib(15))
