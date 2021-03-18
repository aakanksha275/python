a=int(input("enter a"))
b=int(input("enter b"))

try:
    print(a/b)
except Exception as k:
    print("galat")
    print(k)

