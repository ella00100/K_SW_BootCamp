class Graph() :
    def __init__ (self, size) :
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
queue = []
visited_array = []		# 방문한 정점

#정점생성
G1 = Graph(9)

#엣지 생성, 연결
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][4] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1; G1.graph[2][4] = 1; G1.graph[2][5] = 1;
G1.graph[3][1] = 1; G1.graph[3][2] = 1
G1.graph[4][0] = 1; G1.graph[4][2] = 1; G1.graph[4][6] = 1; G1.graph[4][7] = 1
G1.graph[5][2] = 1
G1.graph[6][5] = 1; G1.graph[6][8] = 1
G1.graph[7][4] = 1; G1.graph[7][8] = 1
G1.graph[8][6] = 1; G1.graph[8][7] = 1


#그래프 출력
for row in range(9) :
    for col in range(9) :
        print(G1.graph[row][col], end = ' ')
    print()


#깊이 우선 탐색
current = 0		# 시작 정점 A
queue.append(current)
visited_array.append(current)

while (len(queue) != 0) :
    next = None
    for vertex in range(9) :                #한 행(정점)씩 돌면서
        if G1.graph[current][vertex] == 1 : #연결된 도착점 찾기
            if vertex in visited_array :  	   # 방문한 적이 있는 정점이면 탈락
                pass
            else : 			   # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break

    if next is not None :			  	   # 다음에 방문할 정점이 있는 경우
        current = next                 # 다음으로 이동하여 방문내역 추가
        queue.append(current)
        visited_array.append(current)
    else :            	  	  	  	  # 다음에 방문할 정점이 없는 경우
        current = queue.pop()


print('방문 순서 --> ', end='')
for i in visited_array :
    print(chr(ord('A')+i), end='   ')