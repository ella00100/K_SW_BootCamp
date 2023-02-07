class TreeNode:
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None
data_array = [1, 10, 4, 9, 28, 5, 17]

# 첫 번째 노드 생성
node = TreeNode()
node.data = data_array[0]
root = node
memory.append(node)   # 생성한 노드 메모리에 저장

# 노드 생성, 데이터 추가
for data in data_array[1:] :

	node = TreeNode()
	node.data = data

	current = root 		# 현재 노드를 root로 지정
	while True :
		if data < current.data : 		# 삽입 할 데이터가 현재 노드보다 작고
			if current.left == None :	# 왼쪽 링크가 비었으면
				current.left = node		# 새 노드를 왼쪽 링크로 연결
				break
			current = current.left		# 아니면 왼쪽 노드와 다시 비교
		else :
			if current.right == None :  # 삽입 할 데이터가 더 크면
				current.right = node   	# 새 노드를 오른쪽 링크로 연결
				break
			current = current.right

	memory.append(node)


find_num = 10

current = root
while True :
	if find_num == current.data:
		print(find_num, '을(를) 찾음.')
		break
	elif find_num < current.data :
		if current.left == None :
			print(find_num, '이(가) 트리에 없음')
			break
		current = current.left
	else :
		if current.right == None :
			print(find_num, '이(가) 트리에 없음')
			break
		current = current.right

