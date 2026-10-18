cites={'Алиса':('Боб','Чарли'),'Боб':('Чарли',),'Чарли':()}

rev={}
for author,cited in cites.items():
    
    for c in cited:
        
        if c not in rev:
            rev[c]=set()
        
        rev[c].add(author)

for a in cites:
    if a not in rev:
        rev[a]=set()

print(rev)
