class double_linked_Node():
    def __init__(self):
        self.pre_link = None
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def reverse_print_nodes(head):
    last = head
    while last.link != None:
        last = last.link
    # last : 진짜 last
    current = last

    while current.pre_link != None:
        print(current.data, end = ' ')
        current = current.pre_link
    return


memory = []
head, current, pre, last = [None for _ in range(4)]
data_array = ["피카츄", "파이리", "라이츄", "꼬부기", "버터풀"]

if __name__ == "__main__":
    node = double_linked_Node()
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array:
        pre = node
        node = double_linked_Node()
        node.data = data
        pre.link = node
        node.pre_link = pre
        memory.append(node)

    print_nodes(head)
    reverse_print_nodes(head)

