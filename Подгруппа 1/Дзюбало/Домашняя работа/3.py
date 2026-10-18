def validate_positive(func):
    
    def wrapper(*args):
        for a in args:
            if a<=0:
                return "Ошибка: аргументы должны быть больше нуля"
        
        return func(*args)
    
    return wrapper

@validate_positive
def area(a,b):
    return a*b

print(area(5,3))
print(area(-1,4))
