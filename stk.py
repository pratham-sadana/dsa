class Stk:

    def __init__(self):
        self.stkk = []
   
    def push(self,y):
        self.stkk.append(y)
   
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stkk.pop()
   
    def is_empty(self):
        return len(self.stkk)==0

    def top(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stkk[-1]
