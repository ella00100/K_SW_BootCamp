from operator import itemgetter

class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g):
    print('\t', end = ' ')
    for v in range(g.SIZE):
        print('%-4s' %vertex_array[v], end = ' ')
    print()
    for row in range(g.SIZE):
        print(vertex_array[row], end = ' ')
        for col in range(g.SIZE):
            print("%4d" %g.graph[row][col], end ='  ')
        print()
    print()

def find_vertex(g, find_v):
    stack = []
    visited_array = []

    current = 0
    stack.append(current)
    visited_array.append(current)

    while(len(stack) != 0):
        next = None
        for vertex in range(size):
            if g.graph[current][vertex] != 0:
                if vertex in visited_array:
                    pass
                else:
                    next = vertex
                    break
        if next != None:
            current = next
            stack.append(current)
            visited_array.append(current)
        else:
            current = stack.pop()
    if find_v in visited_array:
        return True
    else:
        return False


size = 6
G = Graph(size)
vertex_array = ["서울", "뉴욕", "런던", "북경", "방콕", "파리"]
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0,1,2,3,4,5

G.graph[서울][뉴욕] = 80; G.graph[서울][북경] = 10
G.graph[뉴욕][서울] = 80; G.graph[뉴욕][북경] = 40; G.graph[뉴욕][방콕] = 70
G.graph[런던][방콕] = 30; G.graph[런던][파리] = 60
G.graph[북경][서울] = 10; G.graph[북경][뉴욕] = 40; G.graph[북경][방콕] = 50
G.graph[방콕][뉴욕] = 70; G.graph[방콕][런던] = 30; G.graph[방콕][북경] = 50; G.graph[방콕][파리] = 20
G.graph[파리][런던] = 60; G.graph[파리][방콕] = 20

print('##   해저 케이블 연결을 위한 전체 연결도   ##')
print_graph(G)

edge_array = []
for i in range(size):
    for k in range(size):
        if G.graph[i][k] != 0:
            edge_array.append([G.graph[i][k],i,k])
edge_array = sorted(edge_array, key = itemgetter(0), reverse=False)

sorted_array = []
for i in range(0, len(edge_array),2):
    sorted_array.append(edge_array[i])

index = 0
while (len(sorted_array) > size-1):
    start = sorted_array[index][1]
    end = sorted_array[index][2]
    save_velocity = sorted_array[index][0]

    G.graph[start][end] = 0
    G.graph[end][start] = 0

    start_TF = find_vertex(G,start)
    end_TF = find_vertex

    if start_TF and end_TF:
        del(sorted_array[index])
    else:
        G.graph[start][end] = save_velocity
        G.graph[end][start] = save_velocity
        index = index + 1

print('##    가장 효율적인 해저 케이블 연결도    ##')
print_graph(G)






