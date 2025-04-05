
class q:
    def __init__(self,size):
        self.size = size
        self.items = []
        self.front = -1
        self.rear = -1

    def isemp(self):
        return self.rear == -1

    def enq(self,n):
        if self.rear == self.size-1:
            print("q is full")
            return
        else:
            self.rear+=1
            self.items[self.rear] = n
            
    def deq(self):
        if q.isemp():
            return "queue is empty!"
        
        self.front = self.items[0]
        for i in range(0,self.rear):
            self.items[i] = self.items[i+1]
        
        rear-=1
        return self.front
    
    def peek(self):
        if q.isemp():
            return "queue is empty!"
        
        return self.items[0]

q = q(5)
q.enq(1)
q.enq(2)
q.enq(3)
q.enq(4)
q.enq(5)
print(q.peek())