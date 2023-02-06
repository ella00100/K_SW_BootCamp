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

def  count_odd_even() :
    '''
    짝수와 홀수 개수를 세는 함수
    :return: int odd개수, even개수
    '''
    global memory, head, current, pre

    odd, even = 0, 0

    current = head
    while True:
        if current.data % 2 == 0:
            even += 1
        else :
            odd += 1
        if current.link == head :
            break
        current = current.link

    return odd, even

def make_minus_number(odd, even):
    '''
    홀수와 짝수 중 많은 쪽을 음수로 만드는 함수
    :param odd: int 홀수의 개수
    :param even: int 짝수의 개수
    :return: void
    '''
    if odd > even :
        reminder = 1
    else :
        reminder = 0

    current = head
    while current.link != head:
        if current.data % 2 == reminder:
            current.data *= -1
        current = current.link


memory = []
head, current, pre = None, None, None


if __name__ == "__main__" :

    dataArray = []
    for _ in range(7) :
        dataArray.append(random.randint(1, 100))

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

    odd_even = count_odd_even()
    print(f'홀수 : {odd_even[0]}개 \t 짝수 : {odd_even[1]}개')

    make_minus_number(odd_even[0],odd_even[1])
    print_node(head)

