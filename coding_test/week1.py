#높이(번호)가 써진 막대기
#입력된 순서대로 번호부여


from sys import stdin

n = int(stdin.readline())
d = [[]for _ in range(n)]
count = 1

for i in range(n):
    d[i] = int(stdin.readline())

#맨 뒤부터 크기가 그 전 막대가 작거나 같으면 안보임
max_bar = d[-1]

for i in range(n-1):
    if max_bar < d[-(i+2)]:
        count += 1
        max_bar = d[-(i+2)]

print(count)


