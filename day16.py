def is_stack_full():
    global size, stack, top
    if top >= size-1:
        return True
    return False

def is_stack_empty():
    global size, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global size, stack, top
    if is_stack_full():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data

def pop():
    global size, stack, top
    if is_stack_empty():
        return
    temp = stack[top]
    stack[top]=None
    top = top-1
    return temp

def peek():
    global size, stack, top
    if is_stack_empty():
        print("Stack is EMPTY!")
        return None
    return stack[top]

size = 4
stack = [None for _ in range(size)]
top = -1

if __name__ == "__main__" :
    with open("진달래꽃.txt",'r',encoding='UTF8') as file:
        line_array = file.readlines()

        print("-----원본-----")
        for line in line_array:
            push(line)
            print(line, end = '')

        print("\n-----거꾸로 처리된 결과-----")
        while True:
            line = pop()
            if line == None:
                break
            small_stack = [None for _ in range(len(line))]
            small_top = -1

            for ch in line:
                small_top += 1
                small_stack[small_top] = ch

            while True:
                if small_top == -1:
                    break
                ch = small_stack[small_top]
                small_top -= 1
                print(ch, end = '')

