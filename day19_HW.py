def insertionSort(ary):
    for end in range(1,len(ary)):
        for cur in range(end, 0, -1):
            if ary[cur-1][1] > ary[cur][1]:
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary

def twobytwo(ary):
    groub = list()
    i = 0
    while i < len(ary):
        groub = ary[i][0],ary[i+1][0]
        i += 2
        print(f'{groub[0]} : {groub[1]}')

data_array = [['선미',88], ['초아',99],['화사',71],['영탁',78],['영웅',67],['민호',92]]
print(f'정렬 전 ---> {data_array}')
sorted_array = insertionSort(data_array)
print(f'정렬 후 ---> {sorted_array}' )
print('## 성적별 조 편성표 ##')
twobytwo(sorted_array)