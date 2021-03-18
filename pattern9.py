# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15


n=int(input("enter number"))

for i in range(1,n+1):
    dec=n-1
    for j in range(1,i+1):
        print(i,end=" ")
        i=i+dec
        dec=dec-1
    print()