import random

def seq_search(ary, find_data):
    pos = -1
    size = len(ary)
    for i in range(size):
        print(ary[i], end = ' ')
        if ary[i] == find_data:
            pos = i
            break
    print()
    return pos

def binary_search(ary, find_data) :
    start = 0
    end = len(ary) - 1
    while (start <= end) :
        mid = (start + end) // 2
        if find_data == ary[mid] :
            return mid
        elif find_data > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1
    return -1

data_ary = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_ary = [random.choice(data_ary) for _ in range(20)]

## 메인 코드 부분 ##
print(f'#오늘 판매된 전체 물건(중복O, 정렬X) --> {sell_ary}')
sell_ary.sort()
print(f'#오늘 판매된 전체 물건(중복O, 정렬O) --> {sell_ary}')
sell_product = list(set(sell_ary))
print('#오늘 판매된 물품 종류(중복x) -->', sell_product)
count_list = []
for product in sell_product :
    count = 0
    pos = 0
    while (pos != -1) :
        pos = binary_search(sell_ary, product)
        if pos != -1 :
            count += 1
            del(sell_ary[pos])
    count_list.append( (product, count))

print()
print("결산 결과 ==>", count_list)
