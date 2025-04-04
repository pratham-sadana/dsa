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

