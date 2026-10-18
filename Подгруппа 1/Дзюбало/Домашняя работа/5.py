sets= [{1,2,3},{2,3,4},{4,5,6}]

from  collections import Counter

c=Counter()
for s in sets:
    for x in s:
        c[x]+=1

uniq=[]
for x,cnt in c.items():
    
    if cnt==1:
        uniq.append(x)

print(sorted(uniq))
