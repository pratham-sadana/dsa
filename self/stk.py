class stk:
    def __init__(self):
        self.items=[]
    def push(self,char):
        self.items.append(char)
    def pop(self):
        return self.items.pop()
    def isemp(self):
        return len(self.items) == 0
    def top(self):
        return self.items[-1]

a = stk()
a.push(4)
a.push(2)
a.pop()
a.push(9)
print(a.items)
