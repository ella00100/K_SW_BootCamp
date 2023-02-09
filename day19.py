def findInsertIdx(ary,data):
    findIdx = -1
    for i in range(0,len(ary)): # 배열의 처음부터 돌면서
        if(ary[i]>data):        # 만약에 data보다 큰 값을 찾아
            findIdx = i         # 삽입 위치를 찾음
            break
    if findIdx == -1:           # 만약 큰 값을 찾지 못했다면
        return len(ary)         # 맨 뒷자리에 위치
    else:
        return findIdx

test_array = [33,100,0,29,88]
sorted_array = []

for i in range(len(test_array)): # test_array를 처음부터 돌면서
    data = test_array[i]         # data에 지정
    ins_pos = findInsertIdx(sorted_array,data) # data의 위치를 찾고
    sorted_array.insert(ins_pos,data) # 찾은 위치에 삽입
print(sorted_array)
