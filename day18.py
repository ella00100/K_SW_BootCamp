class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g):
    print('\t', end = ' ')
    for v in range(g.SIZE):
        print('%8s' %vertex_array[v][0], end = ' ')
    print()
    for row in range(g.SIZE):
        print("%8s" %vertex_array[row][0], end = ' ')
        for col in range(g.SIZE):
            print("\t", g.graph[row][col], end ='\t')
        print()
    print()


G = None
stack = []
visited_array = []

G = Graph(5)
vertex_array = [["GS25",30], ["CU",60], ["Seven11",10], ["MiniStop",90], ["Emart24",40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0,1,2,3,4

G.graph[GS25][CU] =  1; G.graph[GS25][Seven11] = 1
G.graph[CU][GS25] = 1; G.graph[CU][Seven11] = 1; G.graph[CU][MiniStop] = 1
G.graph[Seven11][GS25] = 1; G.graph[Seven11][CU] = 1; G.graph[Seven11][MiniStop] = 1
G.graph[MiniStop][CU] = 1; G.graph[MiniStop][Seven11] = 1; G.graph[MiniStop][Emart24] = 1
G.graph[Emart24][MiniStop] = 1

print_graph(G)

current = 0
stack.append(current)
visited_array.append(current)


for i in range(len(vertex_array)-1):
    maxcount = 0
    maxstore = None
    if vertex_array[i][1] >= vertex_array[i+1][1]:
        maxcount = vertex_array[i][1]
        maxstore = vertex_array[i][0]

print(f'허니버터칩 최대 보유 편의점(개수) --> {maxstore} ( {maxcount} ) ')




