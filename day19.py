import random

def insertionSort(ary):
    for end in range(1,len(ary)):  # 배열의 두번째 자리부터 돌면서
        for current in range(end, 0, -1):   # 앞으로 한자리씩 이동하며
            if (ary[current-1]>ary[current]): # 앞자리가 더 크다면 자리 변경
                ary[current-1], ary[current] = ary[current], ary[current-1]
    return ary

before = [random.randint(0,100) for _ in range(10)]

print(before)
print(insertionSort(before))
