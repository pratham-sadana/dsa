class cirq:
    def __init__(self,size):
        self.size = size
        self.q=[None]*size
        self.front = -1
        self.rear = -1

    def enq(self,item):
        if self.is_full():
            print("Q is full")
            return
        elif self.front == -1:
            self.front = 0
        self.rear = (self.rear+1) % self.size
        self.q[self.rear] = item
        print("Enqueued ",item)
        
    def dq(self):
        if self.is_empty():
            print("Q is empty!")
            return
        else:
            item = self.q[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front+1)%self.size
                print("Dequeued ",item)
        
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def display(self):
        if self.is_empty():
            print("Q is empty")
            return
        else:
            idx = self.front
            while idx != self.rear:
                print(self.q[idx],end="<-")
                if idx == self.rear:
                    break
                idx = (idx+1) % self.size
            print(self.q[self.rear])

cq = cirq(5)
cq.enq(2)
cq.enq(5)
cq.enq(13)
cq.dq()
cq.enq(7)
cq.enq(8)
cq.enq(9)
cq.enq(10)
cq.dq()
cq.dq()
cq.display()