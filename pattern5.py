# P
# P Y
# P Y T
# P Y T H
# P Y T H O
# P Y T H O N

string=input("enter the string")
leng=len(string)
for i in range(1,leng+1):
    for j in range(i):
        print(string[j],end="")
    print()