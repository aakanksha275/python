class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:

    def __init__(self):
        self.head=None
    
    def print_ll(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def delete_beg(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.ref

    def delete_last(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_by_value(self,x):
        if self.head is None:
            print("Empty")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Not present")
        else:
            n.ref=n.ref.ref

ll1=Linkedlist()
ll1.add_begin(50)
ll1.add_begin(800)
ll1.add_begin(30)
#ll1.delete_last()
#ll1.delete_beg()
ll1.delete_by_value(50)
ll1.print_ll()