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

def eval(expr):
    s = stk()
    ex = expr.split()

    for c in ex:
        if c.isdigit():
            s.push(c)
        else:
            b = int(s.pop())
            a = int(s.pop())
            if c == "+":
                s.push(a+b)
            elif c == "-":
                s.push(a-b)
            elif c== "*":
                s.push(a*b)
            elif c == "/":
                s.push(a/b)
    
    return s.pop()
expr = "5 3 + 8 2 - *"
print(eval(expr))