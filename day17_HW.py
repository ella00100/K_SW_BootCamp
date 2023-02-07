import random

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def preorder(node):
    if node == None:
        return
    print(node.data, end= ' ')
    preorder(node.left)
    preorder(node.right)


memory = []
root = None
products = ["바나나맛우유", "레쓰비캔커피", "도시락", "삼각김밥", "코카콜라", "삼다수", "츄파춥스"]
todaysell = [random.choice(products) for _ in range(20)]
print(f'오늘 판매된 물건(중복o) --> {todaysell}')

node = TreeNode()
node.data = todaysell[0]
root = node
memory.append(node)
for name in todaysell[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            break
        elif name < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            current = current.right

print("이진 탐색 트리 구성 완료!")
print('오늘 판매된 종류(중복X)--> ', end = ' ')
preorder(root)
