from itertools import *



"""Task 11*"""
def task_11(A, N, C):
    n = product(A, repeat=int(N))
    num = 0
    for l in n:
        num+=1
        if l[0] == C :
            res = ''
            for x in l : res += x
            print(num, res)
            break


"""Task 12*"""
def task_12(S, N, C1, Sub):
    n = product(S, repeat=int(N))
    kol = 0
    for l in n:
        if len(set(l)) <= 1:
            continue
        if n == C1:
            continue
        res = ''
        for x in l : res += x
        if res.find(Sub):
            continue
        kol += 1



