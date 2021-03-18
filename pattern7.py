#    *
#   * *
#  * * *
# * * * *

n=int(input("enter number"))

'''for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print('\n',end="")'''


i=0
while i<n:
    space=n-i-1
    while space>0:
        print(end=" ")
        space=space-1
    star=i+1
    while star>0:
        print("*",end=" ")
        star=star-1
    i=i+1
    print()