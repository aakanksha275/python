class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
    
class doubly_ll:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head==None:
            print("Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref

    def print_ll_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.pref
                
    def insert_empty(self,data):
        if self.head is None:
            new_n=Node(data)
            self.head=new_n
        else:
            print("Not Empty")

    def insert_beg(self,data):
        new_n = Node(data)
        if self.head is None:
            self.head = new_n
        else:
            new_n.nref = self.head
            self.head.pref = new_n
            self.head = new_n

    def add_end(self,data):
        new_n=Node(data)
        if self.head is None:
            self.head = new_n
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref = new_n
            new_n.pref=n

    def add_after(self,data,x):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Not Present")
            else:
                new_n=Node(data)
                new_n.nref=n.nref
                new_n.pref=n
                if n.nref is not None:
                    n.nref.pref=new_n
                n.nref=new_n

    def add_before(self,data,x):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Not Present")
            else:
                new_n=Node(data)
                new_n.nref=n
                new_n.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_n
                else:
                    self.head=new_n
                n.pref=new_n

dll=doubly_ll()
dll.insert_empty(5)
dll.insert_beg(28)
dll.add_end(55)
dll.add_after(99,5)
dll.add_before(199,5)
dll.print_ll()
dll.print_ll_reverse()

