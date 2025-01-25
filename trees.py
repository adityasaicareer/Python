class node:
    def __init__(self,v):
        self.val=v
        self.left=None
        self.right=None


class tree:
    def __init__(self,n):
        self.head=node(n)
    
    def add(self,n):

        temp=self.head

        while True:

            if(n<temp.val):
                if(temp.left is None):
                    temp.left=node(n)
                    break
                else:
                    temp=temp.left
            else:
                if(temp.right is None):
                    temp.right=node(n)
                    break
                else:
                    temp=temp.right
            

def preorder(temp):
    if(temp!=None):
        preorder(temp.left)
        preorder(temp.right)
        print(temp.val)

def inorder(temp):
    if(temp!=None):
        inorder(temp.left)
        print(temp.val)
        inorder(temp.right)





t=tree(5)
t.add(3)
t.add(7)

preorder(t.head)
print('\n')
inorder(t.head)