# Задача 1
def say_hello_decorator(func):
    def wrapper():
        print("Привет!")
        res = func()
        print("Пока!")
        return res
    return wrapper

@say_hello_decorator
def greet():
    return input()

greet()

# Задача 2
def double_result(func):
    def wrapper():
        return func() * 2
    return wrapper

@double_result
def get_number():
    return int(input())

print(get_number())

# Задача 3
def to_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@to_upper
def get_message():
    return input()

print(get_message())

# Задача 4
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументы: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def multiply(a, b, c=1):
    return a * b * c

args = list(map(int, input().split()))
print(multiply(*args))

# Задача 5
def add_exclamation(func):
    def wrapper():
        res = func()
        if not res.endswith("!"):
            res += "!"
        return res
    return wrapper

@add_exclamation
def say_ok():
    return input()

print(say_ok())

# Задача 6
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def heavy_calc(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

while True:
    line = input()
    if line == "Ок":
        break
    print(heavy_calc(int(line)))

# Задача 7
def positive_only(func):
    def wrapper(*args):
        new_args = [x if x >= 0 else 0 for x in args]
        return func(*new_args)
    return wrapper

@positive_only
def sum_three(a, b, c):
    return a + b + c

print(sum_three(*map(int, input().split())))

# Задача 8
def validate_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                return "Ошибка типов"
        return func(*args)
    return wrapper

@validate_int
def add_nums(a, b):
    return a + b

vals = input().split()
try:
    print(add_nums(int(vals[0]), int(vals[1])))
except ValueError:
    print("Ошибка типов")

# Задача 9
def call_counter(func):
    counts = {}
    def wrapper(word):
        counts[func] = counts.get(func, 0) + 1
        return (func(word), counts[func])
    return wrapper

@call_counter
def ping(word):
    return word

for _ in range(3):
    print(ping(input()))

# Задача 10
def max_length(limit):
    def decorator(func):
        def wrapper():
            res = func()
            if isinstance(res, str) and len(res) > limit:
                return res[:limit] + "..."
            return res
        return wrapper
    return decorator

@max_length(5)
def get_text():
    return input()

print(get_text())
