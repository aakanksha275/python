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

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node

    def add_After(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref = new_node
            
    def add_before(self,data,pos):
        if self.head is None:
            print("Empty")
            return
        if self.head.data==pos:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return

        n=self.head
        while n.ref is not None:
            if n.ref.data==pos:
                break
            n=n.ref
        if n.ref is None:
            print("Node not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node        



ll1=Linkedlist()
ll1.add_begin(50)
ll1.add_end(555)
ll1.add_begin(800)
ll1.add_begin(30)
ll1.add_After(900,555)
ll1.add_before(111,50)
ll1.print_ll()