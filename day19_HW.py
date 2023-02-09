def two_to_one(ary):
    one_array = []
    for i in range(len(ary)):
        for j in range(len(ary)):
            one_array.append(ary[i][j])
    return one_array


def insertionSort(ary):
    for end in range(1,len(ary)):
        for cur in range(end, 0, -1):
            if ary[cur-1] > ary[cur]:
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary

data_array = [[55,33,250,44],
              [88,1,67,23],
              [199,222,38,47],
              [155,245,20,99]]

one_array = two_to_one(data_array)
print(f'1차원 변경 후, 정렬 전 ---> {one_array}')
sorted_array = insertionSort(one_array)
print(f'1차원 변경 후, 정렬 후 ---> {sorted_array}' )
print(f'중앙값 : {sorted_array[len(sorted_array)//2]}')
