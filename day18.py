class Graph:
    def __init__(self,size):
        self.SIZE = size #그래프 크기
        #0으로 초기화된 이차원 배열
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = Graph(4)

#(A,B), (A,C), (A,D)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1

#(B,A), (B,C)
G1.graph[1][0] = 1
G1.graph[1][2] = 1

#(C,A), (C,B), (C,D)
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1

#(D,A), (D,C)
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print("그래프")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()