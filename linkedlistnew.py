class node:
    def __init__(self,n):
        self.val=n
        self.next=None
    
class linked:
    def __init__(self,n):
        self.head=node(n)
    
    def addlast(self,n):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=node(n)
    
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.val)
            temp=temp.next

l=linked(1)
l.addlast(2)
l.addlast(3)
l.display()