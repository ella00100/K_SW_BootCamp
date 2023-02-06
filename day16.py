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

def peek():
    global size, stack, top
    if is_stack_empty():
        print("Stack is EMPTY!")
        return None
    return stack[top]

size = 5
stack = [None for _ in range(5)]
top = -1

if __name__ == "__main__" :
    menu = int(input("1)삽입 2)추출 3)확인 4)종료 :  "))

    while menu != 4 :
        if menu== 1 :
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 : ", stack)
        elif menu== 2 :
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        elif menu== 3 :
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        else :
            print("입력이 잘못됨")

        menu = int(input("1)삽입 2)추출 3)확인 4)종료 :  "))

    print("프로그램 종료!")