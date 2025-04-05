#prathamstack2025final
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

#----------------------------------------------------------------------------------

#prathambfs2025final
def bfs(graph, node): 
  visited = [] 
  queue = []  
  visited.append(node)
  queue.append(node)

  while queue: 
    m = queue.pop(0) 
    print (m) 

    for i in graph[m]:
      if i not in visited:
        visited.append(i)
        queue.append(i)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
bfs(graph, '5') 

#------------------------------------------------------------------------

#prathaminfixtopostfix2025final
from stk import Stk

def infixtopostfix(expr):
    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    operator = "^*/+-"
    postfix = ''
    stack = Stk()  
    
    for char in expr:
        if char.isalnum():  
            postfix += char
        elif char == '(':  
            stack.push(char)
        elif char == ')':  
            while not stack.is_empty() and stack.top() != '(':
                postfix += stack.pop()
            if stack.is_empty():  
                print("Error: Unmatched parentheses")
                return None
            stack.pop()  
        else:  # Operator
            while (not stack.is_empty() and stack.top() in operator and
                   ((prec[stack.top()] > prec[char]) or (prec[stack.top()] == prec[char] and char != '^'))):
                postfix += stack.pop()
            stack.push(char)  

    while not stack.is_empty():  
        if stack.top() == '(' or stack.top() == ')':  
            print("Error: Unmatched parentheses")
            return None
        postfix += stack.pop()
    
    return postfix


# Test case
print(infixtopostfix("a+b*(c^d-e)^(f+g*h)-i"))

#----------------------------------------------------------------------------------

#prathamlinkedlist2025final
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

#-------------------------------------------------------------------------------

#prathamrecursion2025final
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    
n=0
print(fact(n))

def po(x,y):
    if y == 1:
        return 1
    
    return x*po(x,y-1)

x=3
y=3
print(po(x,y))

#
#prathamdfs2025final
def dfs(graph,node,visited=None):
    if visited == None:
        visited = []
    visited.append(node)
    print(node,end =" ")

    for i in graph[node]:
        if i not in visited:
            dfs(graph,i,visited)

graph = {
    'a':['b','c'],
    'b':['d','e'],
    'c':[],
    'd':[],
    'e':['f'],
    'f':['b','c']
}
dfs(graph,'a')

#------------------------------------------------------------------------------

#prathamcircularqueue2025final
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

#----------------------------------------------------------------------------------

#quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left  = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

#postfixeval
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

#paranthesis
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

#doublyll
class Doublyll():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def show(self):
        
        print("showing list data(from head to to tail)")
        current_node = self.head
        while current_node is not None:
            print(current_node.data,"<->",end=" ")
            current_node = current_node.next
        print("None")

    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head= self.tail = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

#queue

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
    
#djikstra
def djik(graph, start):
    d = {node: float('inf') for node in graph}
    d[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or d[node] < d[min_node]):
                min_node = node

        if d[min_node] == float('inf'):
            break

        visited.add(min_node)

        for neighbour, weight in graph[min_node].items():
            new_d = d[min_node] + weight
            if new_d < d[neighbour]:
                d[neighbour] = new_d

    return d

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
sp = djik(graph, start)
print(sp)
