def knapsack():
    print('## 메모이제이션 배열 ##')
    array = [[0 for _ in range(maxWeight+1)] for _ in range(rowCount+1)]	# 빈 배열을 만들고 모두 0으로
    for row in range(1, rowCount+1) :
        print(row, '개 -->', end = ' ')
        for col in range(1, maxWeight+1) :
            if weight[row] > col :	# 물건의 무게가 열보다 크면
                array[row][col] = array[row-1][col]
            else :			# 물건의 부피가 열보다 작거나 같으면
                value1 = money[row] + array[row-1][col-weight[row]]	# 각 그림의 1-1
                value2 = array[row-1][col]
                array[row][col] = max(value1, value2)
            print('%2d' % array[row][col], end = ' ')
        print()
    return array[rowCount][maxWeight]


maxWeight = 7
rowCount = 4
weight = [0, 6, 4, 3, 5]   # 보석 무게 (0, 금괴, 수정, 루비, 진주)
money =  [0,13, 8, 6, 12]  # 보석 가격 (0, 금괴, 수정, 루비, 진주)

if __name__ == "__main__":
    maxValue = knapsack()
    print()
    print('배낭에 담을 수 있는 보석의 최대 가격 -->', maxValue, '억원')