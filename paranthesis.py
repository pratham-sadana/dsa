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


def isValid(expr):
    lefty = "({["
    righty = "]})"
    pairs = {'(':')','[':']','{':'}'}
    s = stk()

    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.isemp():
                return False
            elif c != pairs[s.top()]:
                return False
            s.pop()
    return s.isemp()
print(isValid("A*(B+C*D})+F"))
            

