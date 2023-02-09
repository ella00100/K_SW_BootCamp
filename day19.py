import random

def quickSort(ary):
    global count
    count = count + 1       #반복횟수 count

    if len(ary) <= 1:       # 만약 배열의 길이가 1이하이면
        return ary          # 배열 반환

    pivot = ary[len(ary)//2]     # 기준은 배열의 중간 값
    left_ary, right_ary = [],[]

    for num in ary:         # 배열을 돌면서
        if num < pivot:     # 기준 보다 작으면 왼쪽 배열에 추가
            left_ary.append(num)
        elif num > pivot:   # 기준 보다 크면 오른쪽 배열에 추가
            right_ary.append(num)

    return quickSort(left_ary) + [pivot] + quickSort(right_ary) #재귀 함수 사용

count = 0
data_array = [random.randint(0,200) for _ in range(20)]

print(data_array)
print(quickSort(data_array))
print(count)