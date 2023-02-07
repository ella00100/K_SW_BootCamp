def is_queue_full():
    global SIZE, queue, front, rear
    if ((rear+1)%SIZE == front):
        return True
    else:
        return False

def is_queue_empty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (is_queue_full()):
        print("Queue is FULL")
        return
    rear = (rear+1)%SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("Queue is EMPTY")
        return None
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("Queue is EMPTY")
        return None
    return queue[(front+1)%SIZE]

def time():
    global SIZE, queue, front, rear
    sum_time =0
    for i in range((front+1)%SIZE, (rear+1)%SIZE):
        sum_time += queue[i][1]
    return sum_time

SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":

    data_array = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]
    for data in data_array:
        print(f'귀하의 대기 예상시간은 {time()}분 입니다')
        print(f'현재 대기 콜--> {queue}\n')
        enQueue(data)

    print(f'최종 대기 콜 --> {queue}')
    print('프로그램 종료')