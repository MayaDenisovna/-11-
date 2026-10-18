
d={'Иван': 'Математика', 'Анна': 'Физика', 'Петр': 'Математика'}

inv={}
for name,subj in d.items():
    
    if subj not in inv:
        inv[subj]=[]
    
    inv[subj].append(name)

print(inv)
