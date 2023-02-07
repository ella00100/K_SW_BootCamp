def is_stack_full() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

def is_stack_empty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (is_stack_full()) :
        print("Stack is FULL")
        return
    top += 1
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if (is_stack_empty()) :
        print("Stack is EMPTY")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if (is_stack_empty()) :
        print("Stack is EMPTY")
        return None
    return stack[top]


def check_bracket(expr) :
    for ch in expr:
        if ch in '([{<':           # 여는 괄호는 push
            push(ch)
        elif ch in ')]}>':         # 닫는 괄호는 pop
            out = pop()
            if ch == ')' and out == '(':  # 두 괄호의 짝이 맞으면 pass
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:           # 짝이 맞지 않으면 False
                return False
        else :
            pass
    return is_stack_empty()   # 스택이 비었는지 확인


SIZE = 100
stack = [ None for _ in range(SIZE) ]
top = -1

if __name__ == "__main__":
    expression_array = ["(2*[3+1]", "(A+B)",")A+B(" , "(<A+{B-C}/[C*D]>)"]

    for expression in expression_array:
        top = -1
        print(expression, ":", check_bracket(expression))
    print()