# задание 1
t = (3, 4, 12)
x, y, z = t
r = round((x**2 + y**2 + z**2) ** 0.5, 2)
print(r)

# задание 2
d = {'Иван': 'Математика', 'Анна': 'Физика', 'Петр': 'Математика'}
res = {}
for k, v in d.items():
    res.setdefault(v, []).append(k)
print(res)

# задание 3
def validate_positive(f):
    def w(*a, **kw):
        for i in list(a) + list(kw.values()):
            if i <= 0:
                return "Ошибка: аргументы должны быть больше нуля"
        return f(*a, **kw)
    return w

@validate_positive
def area(a, b):
    return a * b

print(area(3, 4))
print(area(-1, 4))

# задание 4
emp = [
    {'name': 'Иван', 'dept': 'IT', 'salary': 120000},
    {'name': 'Анна', 'dept': 'IT', 'salary': 100000},
    {'name': 'Петр', 'dept': 'HR', 'salary': 70000},
]
s = {}
for e in emp:
    s.setdefault(e['dept'], []).append(e['salary'])
res = {k: round(sum(v) / len(v), 2) for k, v in s.items()}
print(res)

# задание 5
from collections import Counter

sets = [{1, 2, 3}, {2, 3, 4}, {4, 5, 6}]
c = Counter()
for m in sets:
    c.update(m)
res = sorted(k for k, v in c.items() if v == 1)
print(res)

# задание 6
def memoize(f):
    cache = {}
    def w(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return w

@memoize
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))

# задание 7
def merge(a, b):
    r = dict(a)
    for k, v in b.items():
        if k in r and isinstance(r[k], dict) and isinstance(v, dict):
            r[k] = merge(r[k], v)
        else:
            r[k] = v
    return r

d1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
d2 = {'b': {'y': 30, 'z': 40}, 'c': 3}
print(merge(d1, d2))

# задание 8
docs = {1: {'python', 'backend', 'db'}, 2: {'python', 'ai'}, 3: {'backend', 'db'}}
tags = set(input("теги через пробел: ").split())
res = {k for k, v in docs.items() if tags <= v}
print(res)

# задание 9
import time

def profile_func(f):
    def w(*a, **kw):
        st = time.perf_counter()
        r = f(*a, **kw)
        en = time.perf_counter()
        print({'execution_time_sec': en - st})
        return r
    return w

def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)

pfact = profile_func(fact)
print(pfact(10))

# задание 10
cit = {'Алиса': ('Боб', 'Чарли'), 'Боб': ('Чарли',), 'Чарли': ()}
res = {k: set() for k in cit}
for k, v in cit.items():
    for i in v:
        res.setdefault(i, set()).add(k)
print(res)