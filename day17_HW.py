def is_queue_full():
    global SIZE, queue, front, rear
    if (rear == SIZE-1):
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
    if (is_queue_empty()):
        print("Queue is FULL")
        return
    rear += 1
    queue[rear] = data

def deQueue2():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("Queue is EMPTY")
        return None
    else:
        front = front + 1
        data = queue[front]
        queue[front] = None
        current = front
        while current != rear:
            queue[current] = queue[current+1]
            queue[current+1] = None
            current += 1
        front -= 1
        rear -= 1
        return data


def peek():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("Queue is EMPTY")
        return None
    return queue[front+1]

SIZE = 5
queue = ["정국", "뷔", "지민", "진", "슈가"]
front = -1
rear = 4

if __name__ == "__main__":
    while rear != -1:
        print(f'대기 줄 상태 : {queue}')
        print(f'{deQueue2()}님 식당에 들어감')
        print(queue)
        print("\n")
    print("식당 영업 종료!")