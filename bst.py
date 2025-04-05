class Node:
    def __init__(self,data):
        self.left = None
        self.right= None
        self.val = data




def insert(root,new_node):
    if root is None:
        root = new_node
    
    if root.val < new_node.val:
        if root.right is None:
                root.right = new_node
        else:
            insert(root.right,new_node)   
    
    else:
        if root.left is None:
            root.left = new_node
        else:
            insert(root.left,new_node)

def order(root):
    if root:
        order(root.left)
        print(root.val)
        order(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

r = Node(4)
insert(r,Node(5))
insert(r,Node(3))
insert(r,Node(6))
insert(r,Node(2))
insert(r,Node(1))
insert(r,Node(10))
insert(r,Node(9))
insert(r,Node(8))
insert(r,Node(7))

preorder(r)
print("-------------------")
order(r)
print("-------------------")
postorder(r)