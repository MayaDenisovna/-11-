'''
point = tuple(map(int,input().split()))
x, y, z = point
d = (x**2 + y**2 + z**2) ** 0.5
print(round(d, 2))
'''
'''
students = {
    'Иван': 'Математика',
    'Анна': 'Физика',
    'Петр': 'Математика'
}
subjects = dict()
for student, subject in students.items():
    if subject not in subjects:
        subjects[subject] = []
    subjects[subject].append(student)
print(subjects)
'''
'''
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for val in args:
            if val <= 0:
                return "Ошибка: аргументы должны быть больше нуля"
        for val in kwargs.values():
            if val <= 0:
                return "Ошибка: аргументы должны быть больше нуля"
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def pr(a, b):
    return a * b
'''
'''
employees = [
    {'name': 'Иван Красный', 'dept': 'IT', 'salary': 120000},
    {'name': 'Андрей Бурим', 'dept': 'IT', 'salary': 80000},
    {'name': 'Алина Меллстрой', 'dept': 'IT', 'salary': 150000},
    {'name': 'Лысый', 'dept': 'HR', 'salary': 90000},
]

dept_salaries = dict()
for emp in employees:
    dept = emp['dept']
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(emp['salary'])
res = dict()
for dept, salaries in dept_salaries.items():
    avg = sum(salaries) / len(salaries)
    res[dept] = round(avg, 2)

print(res)
'''
'''
sets_list = [{1, 2, 3}, {2, 3, 4}, {4, 5, 6}]
counts = dict()
for s in sets_list:
    for elem in s:
        if elem not in counts:
            counts[elem] = 0
        counts[elem] += 1
res = []
for elem, count in counts.items():
    if count == 1:
        res.append(elem)
res.sort()
print(res)
'''
'''
def memoize(func):
    cache = dict()
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
'''
'''
def deep_merge(dict1, dict2):
    result = dict(dict1)
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
d1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
d2 = {'b': {'y': 30, 'z': 40}, 'c': 3}
merged = deep_merge(d1, d2)
print(merged)
'''
'''
def find_documents(docs, search_tags):
    tags_set = set(search_tags)
    matching_docs = set()
    for doc_id, doc_tags in docs.items():
        if tags_set.issubset(doc_tags):
            matching_docs.add(doc_id)
    return matching_docs
documents = {
    1: {'python', 'backend', 'db'},
    2: {'python', 'ai'},
    3: {'backend', 'db'}
}
user_input = "backend db"
tags = user_input.split()
result = find_documents(documents, tags)
print(result)
'''
'''
import time
def profile_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print({'execution_time_sec': execution_time})
        return result
    return wrapper
@profile_func
def sum_recursive(n):
    if n <= 1:
        return n
    return n + sum_recursive(n - 1)
res = sum_recursive(10)
print(res)
'''
'''
citations = {
    'Алиса': ('Боб', 'Чарли'),
    'Боб': ('Чарли',),
    'Чарли': ()
}
reversed_index = dict()
for author in citations:
    reversed_index[author] = set()
for author, cited_authors in citations.items():
    for cited in cited_authors:
        if cited not in reversed_index:
            reversed_index[cited] = set()
        reversed_index[cited].add(author)
print(reversed_index)
'''