class node:
    def __init__(self,x):
        self.x=x
        self.next=None
    

class list:

    def __init__(self,x):
        self.head=node(x)
    

    def add(self,n):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=node(n)
    
    def display(self):
        temp=self.head
        while temp!=None:
            print(f"{temp.x}->",end="")
            temp=temp.next
        

li=list(1)
li.add(2)
li.add(3)
li.display()
