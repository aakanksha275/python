# A
# B C
# C D E
# D E F G
# E F G H I


n=int(input("enter number of rows"))
k = ord("A")

for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k), end="")
        k+=1
        
    print()