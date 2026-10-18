def deep_merge(d1,d2):
    
    res=d1.copy()
    
    for k,v in d2.items():
        
        if k in res and isinstance(res[k],dict) and isinstance(v,dict):
            res[k]=deep_merge(res[k],v)
        
        else:
            res[k]=v
    
    return res


d1={'a':1,'b':{'x':10,'y':20}}
d2={'b':{'y':30,'z':40},'c':3}

print(deep_merge(d1,d2))
