# Python program to demonstrate 
# insert operation in binary search tree 

# A utility class that represents 
# an individual node in a BST 


class Node: 
	def __init__(self, value): 
		self.left = None
		self.right = None
		self.data = value

# A utility function to insert 
# a new node with the given key 

class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data>node.data:
            node.right=self.insert(node.right,data)
        else:
            node.left=self.insert(node.left,data)
        return node

    def inorder(self,root): 
	    if root: 
		    self.inorder(root.left) 
		    print(root.data) 
		    self.inorder(root.right) 


# Driver program to test the above functions 
# Let us create the following BST 
# 50 
# /	 \ 
# 30	 70 
# / \ / \ 
# 20 40 60 80 

r = Tree()
root=r.createNode(50) 
r.insert(root, 30) 
r.insert(root, 20) 
r.insert(root, 40) 
r.insert(root, 70) 
r.insert(root, 60) 
r.insert(root, 80) 

# Print inoder traversal of the BST 
r.inorder(root) 
