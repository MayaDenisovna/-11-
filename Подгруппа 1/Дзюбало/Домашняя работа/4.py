emps=[{'name': 'Иван', 'dept': 'IT', 'salary': 120000},
      {'name': 'Мария', 'dept': 'HR', 'salary': 90000},
      {'name': 'Петр', 'dept': 'IT', 'salary': 150000},
      {'name': 'Анна', 'dept': 'HR', 'salary': 95000}]

from collections import defaultdict

sums=defaultdict(float)
cnts=defaultdict(int)

for e in emps:
    
    d=e['dept']
    sums[d]+=e['salary']
    cnts[d]+=1


res={}
for d in sums:
    res[d]=round(sums[d]/cnts[d],2)

print(res)
