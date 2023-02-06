import random

class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_node(start) :
    '''
    시작 위치를 인수로 받아 데이터를 출력하는 함수
    :param start: 출력을 시작할 위치
    :return: void
    '''
    current = start         #current는 현재 처리 중인 node
    if current.link == start : #다음 노드가 시작 위치라면 void 반환
        return
    print(current.data, end = ' ')
    while current.link != start:   # 다음 링크가 start가 아닐 때 까지
        current = current.link    #다음 링크로 이동하면서
        print(current.data, end = ' ')  #data 출력
    print()

def count_plus_minus():
    global head, current

    plus, minus, zero = 0, 0, 0

    current = head
    while True:
        if current.data > 0:
            plus = plus + 1
        elif current.data < 0:
            minus = minus + 1
        else:
            zero = zero + 1
        if current.link == head:
            break
        current = current.link

    return plus, minus, zero


def makeSignToggle():
    current = head
    while True:
        current.data = current.data * -1
        if current.link == head:
            break
        current = current.link


memory = []
head, current, pre = None, None, None


if __name__ == "__main__" :

    dataArray = []
    for _ in range(7) :
        dataArray.append(random.randint(-100, 100))

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    print_node(head)

    plus_minus_zero = count_plus_minus()
    print(f'양수 : {plus_minus_zero[0]}개, 음수 : {plus_minus_zero[1]}개, zero : {plus_minus_zero[2]}개')

    makeSignToggle()
    print_node(head)
