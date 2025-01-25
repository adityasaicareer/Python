class node:
    def __init__(self,n):
        self.val=n
        self.next=None


class list:
    def __init__(self,n):
        self.head=node(n)

    
    def add(self,n):

        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=node(n)
    

    def display(self):

        temp=self.head
        while temp is not None:
            print(temp.val)
            temp=temp.next


l=list(1)
l.add(3)
l.add(4)
l.add(5)
l.display()