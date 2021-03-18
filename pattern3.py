# * * * * *
#   *     *
#     *   * 
#       * *
#         * 

n=int(input("enter number"))

for row in range(1,n+1):
    for col in range(1,n+1):
        if row==1 or col==n or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print('\n',end="")