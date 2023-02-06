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
        print("Stack is EMPTY!")
        return
    temp = stack[top]
    stack[top]=None
    top = top-1
    return temp

size = 6
stack = [None for _ in range(6)]
top = -1

if __name__ == "__main__" :
    stone_array = ["주황", "초록", "파랑", "보라","빨강","노랑"]

    print("과자집에 가는길", end = ' ')
    for stone in stone_array:
        push(stone)
        print(f'{stone} --> ', end = ' ')
    print("과자집")

    print("우리집에 가는길", end = ' ')
    while top != -1:
        data = pop()
        print(f'{data} --> ', end = ' ')
    print("우리집")

