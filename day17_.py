class TreeNode() :       #이진 트리의 노드 클래스 선언
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

#root, level 0
node1 = TreeNode()
node1.data = '대표'

#level 1
node2 = TreeNode()
node2.data = '관리이사'
node1.left = node2

node3 = TreeNode()
node3.data = '기술이사'
node1.right = node3

#level 2
node4 = TreeNode()
node4.data = '인사부장'
node2.left = node4

node5 = TreeNode()
node5.data = '회계부장'
node2.right = node5

node6 = TreeNode()
node6.data = '연구부장'
node3.left = node6

#complete binary tree 완성

print(node1.data, end = ' ')
print()
print(node1.left.data,  node1.right.data, end = ' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end = ' ')



