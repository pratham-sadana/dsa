class q:
    def q(self,size):
        self.arr = []
        self.size = size
        self.rear = -1
        self.front = -1

    def isempty(self):
        return self.rear == -1
    
    def enq(self,data):
        if self.rear == self.size-1:
            print("Queue is full!")
            return
        else:
            rear+=1
            self.arr[rear] = data

    def deq(self):
        if self.isempty():
            print("Queue is empty!")
            return -1
        self.front=self.arr[0]
        for i in range(0,self.rear):
            self.arr[i] = self.arr[i+1]
        rear -=1
        return self.front
    
    def peek(self):
        if self.isempty():
            print("Queue is empty!")
            return -1
        return self.arr[0]
    

ab = q()
ab.enq(1)
ab.enq(2)
ab.deq()
ab.enq(1)        
ab.enq(3)
ab.enq(6)
ab.enq(8)
while not ab.isempty():
      print(ab.peek())
      ab.deq()
    


