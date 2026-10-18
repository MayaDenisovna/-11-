

docs={1:{'python','backend','db'},2:{'python','ai'},3:{'backend','db'}}

tags=['backend','db']

res=set()
for id,tgs in docs.items():
    
    if all(t in tgs for t in tags):
        res.add(id)

print(res)
