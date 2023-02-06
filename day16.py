import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_stores(start):
    """
    지정 위치 부터 마지막 노드의 데이터 까지 출력 형식에 맞춰 출력 하는 함수
    :param start: str 시작위치
    :return: void
    """
    current = start         # 현재 위치는 지정 위치
    if current == None:
        return

    while current.link != head:     # 마지막 노드까지 반복
        current = current.link
        x,y = current.data[1:3]
        print(f'{current.data[0]}편의점, 거리 : {math.sqrt(x*x+y*y)}')


def make_sorted_store(store):
    """

    :param store: list(편의점 이름, x좌표, y좌표)
    :return:
    """
    global memory, head, current, pre

    node = Node()           # 노드 생성
    node.data = store       # 노드에 데이터 지정
    memory.append(node)

    if head == None:        # 만약 첫 번째 노드 라면
        head = node         # head로 지정
        node.link = head    # circular linked list이므로 자기 자신을 link
        return

    x, y = node.data[1:3]   # x = x좌표, y = y좌표
    dist = math.sqrt(x*x+y*y) # dist 구하기

    head_x,head_y = head.data[1:3] # head의 x, y, dist 구하기
    head_dist = math.sqrt(head_x*head_x + head_y*head_y)

    if head_dist > dist:           # head의 dist 보다 작다면
        node.link = head           # node.link = head
        head = node                # 현재 node를 head로 지정
        last = head                # last = head
        while last.link != head:   # last가 마지막이 될때 까지 last 한칸 씩 미뤄주기
            last = last.link
        last.link = head           # 마지막 노드 head와 연결
        return

    current = head                 # 첫 번째 노드가 아니 라면
    while current.link != head:
        pre = current
        current = current.link
        current_x, current_y = current.data[1:]
        current_dist = math.sqrt(current_x*current_x+current_y*current_y)
        if current_dist > dist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


memory = []
head, current, pre = [None for _ in range(3)]

if __name__ == "__main__" :

    stores_array = []
    store_name = "A"
    for _ in range(10):
        x,y = random.randint(1,100), random.randint(1,100)
        store = (store_name, x, y)
        stores_array.append(store)
        store_name = chr(ord(store_name)+1)

    for store in stores_array:
        make_sorted_store(store)

    print_stores(head)


