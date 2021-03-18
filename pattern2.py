# *
# * * 
# * * * 
# * * * *
# * * * * *

n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or i==j:
            print("*",end="")
        else:
            print(end=" ")
    print('\n',end="")