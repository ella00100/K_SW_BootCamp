# Node 데이터형 생성
class Node():           #Node 객체는 data와 link 속성을 가짐
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
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None:   #비워 있지 않을 때 까지 (마지막 위치 까지) 반복
        current = current.link    #다음 링크로 이동
        print(current.data, end = ' ')  #data 출력
    print()

def insert_node(find_data, insert_data) :
    '''
    지정한 위치(find_data 이전)에 새로운 노드를 삽입하는 함수
    :param find_data: str 찾을 node.data (지정 위치)
    :param insert_data: str 삽입할 node.data
    :return: void
    '''
    global memory, head, current, pre   #head는 첫번째 node, pre는 이전 노드

    if head.data == find_data :      # 만약 find_data가 첫 노드라면
        node = Node()                # 새로운 node 생성 , head 자리에 삽입
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link != None :    # 중간에 위치한 노드라면
        pre = current               # 탐색
        current = current.link
        if current.data == find_data : #find_data의 위치를 찾으면
            node = Node()              # 그 앞에 새로운 node 생성 , 삽입
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()                   # 마지막 노드 삽입
    node.data = insert_data
    current.link = node


def delet_node(delet_data) :
    '''
    노드를 삭제하는 함수
    :param delet_data: str 삭제할 데이터
    :return: void
    '''
    global memory, head, current, pre

    if head.data == delet_data :     # 첫 번째 노드 삭제
        print("첫번째 노드 삭제 완료")
        current = head
        head = head.link             # head를 한 칸 미룸
        del(current)                 # 현재 위치 노드 삭제
        return

    current = head                          # 첫 번째  외 노드 삭제
    while current.link != None :            # 탐색
        pre = current
        current = current.link
        if current.data == delet_data :     #delet_data의 위치를 찾으면
            print("중간 노드 삭제 완료")
            pre.link = current.link         #이전 link와 현재 link를 이어준 뒤
            del(current)                    #현재 위치 노드 삭제
            return

    print("삭제할 노드를 찾지 못함")

def find_node(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link != None:
        crrent = current.link
        if current.data == find_data:
            return current

    return Node(None)


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()			# 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :		# 두 번째 노드 부터 마지막 까지
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_node(head)

    insert_node("피카츄", "잠만보")
    print_node(head)
    insert_node("버터풀", "라도란")
    print_node(head)

    delet_node("잠만보")
    print_node(head)
    delet_node("라도란")
    print_node(head)
    delet_node("둥이")
    print_node(head)

    print(find_node("피카츄").data)
    print(find_node("둥이").data)


