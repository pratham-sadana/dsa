class Stk:

    def __init__(self):
        self.stkk = []
   
    def push(self,y):
        self.stkk.append(y)
   
    def pop(self):
        x = self.stkk[-1]
        del self.stkk[(len(self.stkk)-1)]
        return x
   
    def is_empty(self):
        if len(self.stkk)==0:
            return True
        else:
            return False

    def top(self):
        return self.stkk[-1]

x = Stk()
x.push(1)
x.push(5)
x.push(8)
z = x.pop()
x.push(3)
print(z)
print(x.top())
print(x.stkk)