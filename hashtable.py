def hash_key( key, m):
    return key % m



listy=[3,2,9,11,7]
m=len(listy)
for i in listy:
    k=hash_key(i,m)
    print(k)
