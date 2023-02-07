def is_queue_full() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :       #real이 size-1 이 아니면 꽉 차지 않은 것
        return False
    elif (rear == SIZE -1) and (front == -1) : #real이 size-1이고, front=-1이면 무조건 full
        return True
    else : #real이 size-1이나 front가 -1이 아닌 경우
        for i in range(front+1, SIZE) : # front+1부터 rear 위치까지
            queue[i-1] = queue[i]       # queue를 한칸씩 땡기기
            queue[i] = None             # 맨 뒷 자리 비워주기
        front -= 1                      #front와 real 1씩 감소
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (is_queue_full()) :   #만약 큐가 가득 찼다면 enQueue 불가
        print("Que is Full")
        return
    rear += 1           # 아니라면 real 1 증가
    queue[rear] = data  # real 자리에 data 삽입

def is_queue_empty() :
    global SIZE, queue, front, rear
    if (front == rear) :   #front와 que가 같다면 큐가 비어있는 것
        print("Que is EMPTY")
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (is_queue_empty()) :   #큐가 비어있으면 데이터 추출 불가
        print("Que is EMPTY")
        return None
    front += 1          # 아니라면 front 1 증가
    data = queue[front] # front 자리 데이터 추출
    queue[front] = None # front 자리 비우기
    return data

def peek() :
    global SIZE, queue, front, rear
    if (is_queue_empty()) :
        print("Que is EMPTY")
        return None
    return queue[front+1] #que의 가장 앞에 있는 데이터 확인



SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1

enQueue("강아지")
enQueue("고양이")
print(queue)
print(peek())
print(queue)
