import random

def seq_search(ary, find_data) :
    global count
    pos = -1
    for i in range(len(ary)) :
        count += 1
        if ary[i] == find_data :
            pos = i
            break
    return pos

def binary_search(ary, find_data) :
    global count
    start = 0
    end = len(ary) - 1

    while (start <= end) :
        count += 1
        mid = (start + end) // 2

        if find_data == ary[mid] :
            return mid
        elif find_data > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return -1

data_ary= []
find_data = 121922
count = 0

data_ary = [random.randint(0, 999999) for _ in range(1000000)]
data_ary.insert(random.randint(0, 1000000), find_data)

count = 0
print(f'#비정렬 배열(100만개) --> {data_ary[0:5]} ~~~~ {data_ary[-5:len(data_ary)]}')
pos_seq = seq_search(data_ary,find_data)
count_seq = count

data_ary.sort()
count = 0
print(f'#정렬 배열(100만개) --> {data_ary[0:5]} ~~~~ {data_ary[-5:len(data_ary)]}')
pos_binary = binary_search(data_ary, find_data)
count_binary = count


print(f'순차 검색(비정렬 데이터) --> {count_seq}회')
print(f'이진 검색(정렬 데이터) --> {count_binary}회')
