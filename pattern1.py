# 1
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print('\n',end="")