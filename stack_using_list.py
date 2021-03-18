stack=[]

def push():
    if len(stack)==n:
        print("Stack is Full")
    else:
        e=int(input("enter element to push"))
        stack.append(e)
        print(f"The stack is {stack}")

def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        e= stack.pop()
        print(f"Removed element is {e} and final stack is {stack}")


n=int(input("Enter the number of elements to want to enter"))
while True:
    print("Enter 1 to push , 2 for pop and 3 to quit")
    user=int(input())
    if user==1:
        push()
    elif user==2:
        pop()
    elif user==3:
        print("Thank you!")
        break
    else:
        print("Please enter a valid choice")