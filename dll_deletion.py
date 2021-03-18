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

    def delete_beg(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.nref is None:
            self.head=None
            print("empty after 1st node is deleted")
        else:
            self.head=self.head.nref
            self.head.pref=None
   
    def delete_end(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.nref is None:
            self.head=None
            print("empty after 1st node is deleted")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("Empty")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print("Not Present")
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref =None
            else:
                print("Not Present")

    

dll=doubly_ll()
dll.insert_empty(5)
dll.insert_beg(28)
dll.insert_beg(2)
dll.insert_beg(8)
dll.insert_beg(100)
dll.delete_beg()
dll.delete_end()
dll.delete_by_value(28)
dll.print_ll()

