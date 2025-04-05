class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class doublyll:
    head =None
    tail = None

    def append(self,data):
        node = Node(data,None,None)
        if self.head is None:
            self.head = self.tail = node
        else:
            pr = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.prev = pr

    def show(self):
        temp = self.head
        print("here it goes: ")
        while temp is not None:
            print(temp.data,"<->",end=" ")
            temp = temp.next
        print(None)

d =doublyll()
d.append(5)
d.append(2)        
d.append(1)
d.append(12)
d.show()
    
