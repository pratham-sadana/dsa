class Node(object):
 
    def __init__(self, data, next):
        self.data = data
        self.next = next
 
 
class SingleList(object):
 
    head = None
    tail = None
 
    def show(self):
        print("Showing list data:")
        current_node = self.head
        while current_node is not None:
            print (current_node.data, " -> ")
            current_node = current_node.next
        print(None)
 
    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node
s = SingleList()
s.append(31)
s.append(2)
s.append(3)
s.append(4)
s.show()