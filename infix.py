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
print(infixtopostfix("a+b*(c^d-e)^(f+g*h)-i"))  # Expected output: "abcd^e-fgh*+^*+i-"
