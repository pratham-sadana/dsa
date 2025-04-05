class Node:
    def __init__(self,data, next= None):
        self.data= data
        self.next = next

class singlyll:
    head = None
    tail = None
    
    def append(self,nn):
        node = Node(nn,None)
        if self.head is None:
            self.head= self.tail = node
        else:
            self.tail.next=node
        self.tail = node
            

    def show(self):
        temp = self.head
        print("Singly Linked List:",end=" ")
        while temp is not None:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print(None)

s = singlyll()
s.append(31)
s.append(2)
s.append(3)
s.append(4)
s.show()
